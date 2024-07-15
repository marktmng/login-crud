from django.db import models
from django.contrib.auth.models import User #import user model

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    members = models.ManyToManyField(User, related_name="chat_room_pytmembers")
    
    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField()
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text + "" + self.user.username