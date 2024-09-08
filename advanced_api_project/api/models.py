from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name with a max of 255 words.

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title for the book.
    publication_year = models.IntegerField()  # Publication year of the book.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # One-to-many relationship between author and the many books they write.

    def __str__(self):
        return self.title

