from django.urls import path, include
from .views import BookList  # Imports the BookList view
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Map '/books/' to the BookList view
    path('', include(router.urls)),
]

