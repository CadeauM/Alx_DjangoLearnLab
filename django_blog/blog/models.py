from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) 
    content = models.TextField() 
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    def __str__(self):
        return self.title
    
class Comment(models.Model): # This is the Comment model. It's a blueprint for every comment in the system.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Each comment belongs to a specific blog post. If the post gets deleted, the comment should too.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()   # This is the actual text of the comment.
    created_at = models.DateTimeField(auto_now_add=True)  # this saves the time when the comment was created automatically.
    updated_at = models.DateTimeField(auto_now=True)  # Saves the time when the comment was last updated.
    
    def __str__(self):  # makes the posts readable
        return f'Comment by {self.author} on {self.post}'

