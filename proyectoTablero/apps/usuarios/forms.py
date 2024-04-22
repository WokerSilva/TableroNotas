from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        #fields = ('username', 'password1', 'password2', 'fecha_nacimiento')
        fields = ['username', 'fecha_nacimiento', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")

        return cleaned_data

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')