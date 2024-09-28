from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actor')
    verb = models.CharField(max_length=255)  # A short description of the action (e.g., "liked your post")
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    target_object_id = models.PositiveIntegerField(null=True) 
    target = GenericForeignKey('target_content_type', 'target_object_id')  # This allows linking to any object (e.g., a post or comment)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Whether the notification has been read or not
    
    def __str__(self):
        return f'{self.actor} {self.verb} {self.target}'

