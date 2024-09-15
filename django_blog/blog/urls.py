from django.urls import path
from django.contrib.auth import views as auth_views  # we are importing the login/logout views
from . import views   # we are importing the views we have create for registration and profile.

# Defining the paths for login, logout, registration, and profile
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'), 
]
