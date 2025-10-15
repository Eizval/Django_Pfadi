from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm
from django.contrib import messages


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
    return render(request, "accounts/approve.html", {})
