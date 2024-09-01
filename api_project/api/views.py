from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book  # Imports the Book model
from .serializers import BookSerializer  # Imports the BookSerializer from the serializer file
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query all Book objects
    serializer_class = BookSerializer  # Specifies the serializer to use

class BookViewSet(viewsets.ModelViewSet):  # This is a viewset for viewing and editing book instances
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
