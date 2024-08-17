from django.urls import path  # Correct import statement
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index page of the relationship_app
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
