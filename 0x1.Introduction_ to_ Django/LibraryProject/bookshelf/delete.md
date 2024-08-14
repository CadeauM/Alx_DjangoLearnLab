# Delete the book you created and confirm the deletion by trying to retrieve all books again
from bookshelf.models import Book
book_to_delete = Book.objects.get("Nineteen Eight-Four")
book_to_delete.delete()

all_books = Book.objects.all
print(all_books)
