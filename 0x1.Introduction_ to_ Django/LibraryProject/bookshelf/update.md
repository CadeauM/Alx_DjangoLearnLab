# Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
from bookshelf.models import Book
update_book = Book.objects.get(title = "1984")
update_book.title = "Nineteen Eighty-Four"
update_book.save()
print(update_book)