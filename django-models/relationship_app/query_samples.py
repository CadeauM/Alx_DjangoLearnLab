from relationship_app.models import Author, Book

# Query All Books by a Specific Author
def all_books_by_author(author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author)
    return books

# List All Books in a Library
from relationship_app.models import Library, Book
def all_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    return books

# Retrieve the Librarian for a Library
from relationship_app.models import Library, Librarian
def librarian_to_library(library_id):
    library = Library.objects.get(id=library_id)
    librarian = Librarian.objects.get(library=library)
    return librarian
