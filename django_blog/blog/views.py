from django.shortcuts import render
from django.shortcuts import render 
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm  # Importing the forms file
from django.contrib.auth.decorators import login_required  # Ensures only logged-in users can access the profile page

# Create your views here.
# This will handle the view that handles user registration
def register(request):
    if request.method == 'POST':  # the user submits the form
        form = UserRegisterForm(request.POST)  # Fill the form with submitted data
        if form.is_valid():  # check if form is valid then save it. 
            form.save() 
            messages.success(request, 'Your account has been created, you can log in.')  # success message!
            return redirect('login')  # redirects to login page.
        else:
            form = UserRegisterForm()  # user just checking page.
            return render(request, 'blog/register.html', {'form': form})

@login_required  # this is a decorator.
def profile(request):
    return render(request, 'blog/profile.html')  # This shows the profile page
