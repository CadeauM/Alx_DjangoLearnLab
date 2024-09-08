from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    # Serializer for the Book model. This serializer validates the publication year to ensure it's not in the future.
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
    # Check that the publication year is not in the future.

        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Serializer for the Author model.This serializer nests the books related to the author.

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

