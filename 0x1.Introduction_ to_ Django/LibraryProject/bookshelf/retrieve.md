# Retrieve and display all attributes of the book
all_books = Book.objects.all()
for book in all_books:
    print(book.title, book.author, book.publication_year)