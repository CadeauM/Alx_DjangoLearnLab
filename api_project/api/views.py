from django.shortcuts import render
from rest_framework import generics
from .models import Book  # Imports the Book model
from .serializers import BookSerializer  # Imports the BookSerializer from the serializer file

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query all Book objects
    serializer_class = BookSerializer  # Specifies the serializer to use

