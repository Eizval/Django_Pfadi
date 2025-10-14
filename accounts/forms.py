from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# ----------------------
# Login-Form
# ----------------------

class UserLoginForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )


# ----------------------
# Register-Form
# ----------------------

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    email = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']