from rest_framework import serializers
from .models import Book  # This Imports the Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specifies the model to serialize
        fields = '__all__'  # this icludes all the fields from the book model.

