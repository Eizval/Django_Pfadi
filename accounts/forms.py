from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Role


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
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Allen Feldern Bootstrap-Style geben
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # Optionale Platzhalter:
            if field_name == 'password1':
                field.widget.attrs['placeholder'] = 'Passwort'
            elif field_name == 'password2':
                field.widget.attrs['placeholder'] = 'Passwort bestätigen'


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class RoleCreateForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }