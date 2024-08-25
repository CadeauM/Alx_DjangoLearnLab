# Create a Book instance
from bookshelf.models import Book
>>> new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(new_book)
1984
# Retrieve and display all attributes of the book
all_books = Book.objects.all()
for book in all_books:
...  print(book.title, book.author, book.publication_year)
...
1984 George Orwell 1949
# Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
book_to_update = Book.objects.get(title="1984")
>>> book_to_update.title = "Nineteen Eighty-Four"
>>> book_to_update.save()
>>> print(book_to_update)
Nineteen Eighty-Four
# Delete the book you created and confirm the deletion by trying to retrieve all books again
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
>>> book_to_delete.delete()
(1, {'bookshelf.Book': 1})
>>> all_books = Book.objects.all()
>>> print(all_books)
<QuerySet []>
>>> exit()