from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)  #this registers the Book model with the django admin site
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # this will show the details of each book in the admin panel
    search_fields = ('title', 'author')  # you can then search the books in the panel by the title or author
    list_filter = ('publication_year',) # the filter to the sidebar so if you need you can search the books by their publication year
