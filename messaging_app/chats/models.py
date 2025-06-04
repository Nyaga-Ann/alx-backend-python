from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Extended User model
class User(AbstractUser):
    # Add any extra fields you want here
    bio = models.TextField(blank=True, null=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Conversation model
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


# Message model
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.username} in Conv {self.conversation.id}: {self.content[:30]}"
