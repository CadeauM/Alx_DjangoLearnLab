from django.urls import path
from .views import BookList  # Imports the BookList view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Map '/books/' to the BookList view
]

