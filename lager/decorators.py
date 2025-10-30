from django.http import HttpResponseForbidden
from functools import wraps

def role_or_superuser_required(role_id):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and (user.role_id == role_id or user.is_superuser):
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Du hast keine Berechtigung.")
        return _wrapped_view
    return decorator
