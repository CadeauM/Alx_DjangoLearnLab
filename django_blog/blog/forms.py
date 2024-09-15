from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # This is Django’s built-in user model

from .models import Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CommentForm(forms.ModelForm):  # This form is based on the Comment model.
    class Meta:
        model = Comment  # We are using the Comment model to generate this form.
        fields = ['content']   # The form will only need the content field
        
