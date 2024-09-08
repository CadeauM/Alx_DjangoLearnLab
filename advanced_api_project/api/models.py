from django.db import models

# Create your models here.
class Author(models.Model):  # The name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):  
    title = models.CharField(max_length=255)  # The title of the book
    publication_year = models.IntegerField()  # The year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
     # ForeignKey relationship with Author model
    # Each book has one author, and an author can have many books
    def __str__(self):
        return self.title

