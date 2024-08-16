from relationship_app.models import Book

# Query All Books by a Specific Author

def all_books_by_author(author_name):
    Author.objects.get(name=author_name)"
    return Book.objects.filter(author=author)

# List All Books in a Library

def all_books_in_library(library_name):
    Library.objects.get(name=library_name)
    return books.all()

# Retrieve the Librarian for a Library

def librarian_to_library(library_id):
    return Librarian.objects.filter(library_id=library_id).first()
