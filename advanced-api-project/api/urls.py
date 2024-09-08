from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # URL for retrieving all books or adding a new book
    path('books/', BookListView.as_view(), name='book-list'),
    
    # URL for retrieving, updating, or deleting a specific book by its ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # URL for creating a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    
    # URL for updating an existing book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    
    # URL for deleting a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
