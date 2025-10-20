from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth import logout

User = get_user_model()

# Create your views here.
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


def logout_view(request):
    logout(request)
    return redirect('login')
