from django.conf import settings
from django.db import models
from datetime import datetime

# модель, що відповідає за чат
class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(null=True)
    base64 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.message
    
# модель, що відповідає за чат
class UserChatModel(models.Model):
    sourceId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sourceId")
    targetId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="targetId")
    message = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now())
    updatedAt = models.DateTimeField(null=True)

    class Meta:
        db_table = "user_message"
        
# модель що відповідає за підписки
class Relationships(models.Model):
    followerUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followerUserId")
    followedUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followedUserId")
    
    class Meta:
        db_table = "relationships"

