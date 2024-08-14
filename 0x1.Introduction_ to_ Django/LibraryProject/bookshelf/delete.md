# Delete the book you created and confirm the deletion by trying to retrieve all books again
from bookshelf.models import Book
book = Book.objects.get("Nineteen Eight-Four")
book.delete()

all_books = Book.objects.all
print(all_books)
