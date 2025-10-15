from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login_view(request):
    return render(request, "accounts/login.html", {})

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


def approve_view(request):
    unapproved_users = User.objects.filter(is_approve=False)

    return render(request, "accounts/approve.html", {"users": unapproved_users})


@user_passes_test(lambda u: u.is_superuser)
def approve_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.is_approve = True  # oder user.is_approved je nach Feld
        user.save()
        messages.success(request, f'{user.username} wurde genehmigt!')
    return redirect('approve')
