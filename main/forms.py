from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, required=True)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']