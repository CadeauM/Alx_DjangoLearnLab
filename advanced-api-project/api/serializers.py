from rest_framework import serializers
from .models import Author, Book
from .models import Book
import datetime

# BookSerializer: Handles serialization of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# AuthorSerializer: Handles serialization of the Author model, including nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested books in the author serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # `books` shows nested book data

