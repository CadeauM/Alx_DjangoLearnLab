from django.urls import path  # Correct import statement
from .views import LibraryDetailView
from . import views

from .views import LoginView, LogoutView, register
from .views import admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books

urlpatterns = [
    path('', views.index, name='index'),  # Index page of the relationship_app
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('eedit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
    
]
