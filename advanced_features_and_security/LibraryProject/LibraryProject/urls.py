from django.contrib import admin
from django.urls import path
from bookshelf.views import (
    LibraryDetailView,
    list_books,
    add_book,
    edit_book,
    delete_book,
    index,
    register,
    librarian_view,
    member_view
)
from bookshelf.views import list_books, add_book, edit_book, delete_book, index, register, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView
from bookshelf.views import add_book, edit_book
from bookshelf.views import index


urlpatterns = [
    path('', index, name='index'),  # Index page of the bookshelf app
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
]