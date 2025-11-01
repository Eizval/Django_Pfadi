from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserRegistrationForm, RoleForm
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth import logout

from accounts.models import Role

User = get_user_model()


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    # Wenn Formular gesendet wird

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Prüft, ob User existiert und Passwort korrekt ist
        user = authenticate(request, username=username, password=password)

        # Wenn Login erfolgreich
        if user is not None:
            # Prüft, ob Account vom Admin freigegeben wurde
            if user.is_approve:
                login(request, user)
                return redirect('lager_list')  # z. B. deine Startseite
            else:
                messages.warning(request, 'Dein Account wurde noch nicht freigegeben.')
        else:
            messages.error(request, 'Ungültiger Benutzername oder Passwort.')

    # GET → Seite anzeigen
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrierung erfolgreich! Du kannst dich jetzt einloggen.")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def approve_view(request):
    unapproved_users = User.objects.filter(is_approve=False)

    context = {
        "users": unapproved_users,
        "role_url": "/role/",  # oder nutze reverse('role') wenn URL-Name gesetzt
        "allusers_url": "/all_users/"  # oder reverse('allusers')
    }
    return render(request, "accounts/approve.html", context)


# @login_required
# @user_passes_test(lambda u: u.is_superuser)
def approve_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.is_approve = True  # oder user.is_approved je nach Feld
        user.save()
        messages.success(request, f'{user.username} wurde genehmigt!')
    return redirect('approve')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def all_users_view(request):
    allusers = User.objects.all()
    return render(request, "accounts/allusers.html", {"objects": allusers})

    # sort = request.GET.get('sort', 'id')  # Standardsortierung nach ID
    # direction = request.GET.get('dir', 'asc')  # Standard: aufsteigend
    # if direction == 'desc':
    #     sort = f'-{sort}'  # minus für absteigend
    # allusers = User.objects.all().order_by(sort)
    # context = {
    #     "objects": allusers,
    #     "current_sort": request.GET.get('sort', 'id'),
    #     "current_dir": request.GET.get('dir', 'asc')
    # }
    # return render(request, "accounts/allusers.html", context)


# def user_list(request):
#     users = User.objects.all()
#     columns = [
#         ('id', 'ID'),
#         ('username', 'Username'),
#         ('email', 'Email'),
#         ('is_staff', 'Staff?'),
#         ('is_superuser', 'Superuser?'),
#         ('is_approve', 'Approved?')
#     ]
#     current_sort = request.GET.get("sort", "")
#     current_dir = request.GET.get("dir", "asc")
#     return render(request, "user_list.html", {
#         "objects": users,
#         "columns": columns,
#         "current_sort": current_sort,
#         "current_dir": current_dir
#     })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def role_view(request):
    roles = Role.objects.all()
    return render(request, "accounts/role.html", {"objects": roles})


# ---------- Rollen zu Benutzer hinzufügen ----------
@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_role_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    roles = Role.objects.all()

    if request.method == 'POST':
        selected_role_id = request.POST.get('roles')  # nur eine Rolle erlaubt
        if selected_role_id:
            user.role_id = selected_role_id  # direkte FK-Zuweisung
            user.save()
            return redirect('all_users')
    context = {'user': user, 'roles': roles}
    return render(request, 'accounts/add_role.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_role_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role:
            Role.objects.get_or_create(name=role)
            return redirect('role')
    return render(request, 'accounts/create_role.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_role_view(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    has_users = User.objects.filter(role=role).exists()
    if has_users:
        messages.error(request, 'Du kannst diese Rolle nicht Löschen da ein User diese Rolle besitzt.')
    else:
        role.delete()
        messages.success(request, "Rolle wurde erfolgreich gelöscht.")
    return redirect('role')
