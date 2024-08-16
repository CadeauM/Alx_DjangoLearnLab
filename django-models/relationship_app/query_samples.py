from relationship_app.models import Book

# Query All Books by a Specific Author

def all_books_by_author(author_name):
    return Book.objects.filter(author_name=author_name)

# List All Books in a Library

def all_books_in_library():
    return Book.objects.all()

# Retrieve the Librarian for a Library

def librarian_to_library(library_id):
    return Librarian.objects.filter(library_id=library_id).first()
