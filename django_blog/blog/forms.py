from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # This is Django’s built-in user model


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
