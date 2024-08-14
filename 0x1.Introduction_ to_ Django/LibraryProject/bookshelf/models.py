from django.db import models

# Create your models here.
class Book(models.Model):  #we are defining the book model
    title = models.CharField(max_length=200)  #title has a max of 200 characters
    author = models.CharField(max_length=100)  #author has a max of 100 characters
    publication_year = models.IntegerField()  #the year the book was published

    def __str__(self):  #here when we print the instance of the book class we'll see the books title in return.
        return self.title
    