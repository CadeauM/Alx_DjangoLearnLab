from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # This is Django’s built-in user model

from .models import Comment
from .models import Post
from taggit.forms import TagWidget


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CommentForm(forms.ModelForm):  # This form is based on the Comment model.
    class Meta:
        model = Comment  # We are using the Comment model to generate this form.
        fields = ['content']   # The form will only need the content field
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Includes 'tags' in the form
        widgets = {
            'tags': TagWidget(),  # This will display a nice tag input widget
        }

