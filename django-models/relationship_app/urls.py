from django.urls import path
from . import views

urlpatterns = [
    # Define your app's URL patterns here
    path('', views.index, name='index'),
]