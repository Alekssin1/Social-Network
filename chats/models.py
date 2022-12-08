from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(null=True)
    base64 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.message


class UserChatModel(models.Model):
    sourceId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sourceId")
    targetId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="targetId")
    message = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now())
    updatedAt = models.DateTimeField(null=True)

    class Meta:
        db_table = "user_message"
        
class Relationships(models.Model):
    followerUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followerUserId")
    followedUserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followedUserId")
    
    class Meta:
        db_table = "relationships"

class UserPost(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    createdAt = models.DateTimeField(default=datetime.now())
    content = models.ManyToManyField("Photo")

    class Meta: 
        db_table = "user_post"
        
class Photo(models.Model):
    photo = models.FileField(upload_to='uploads/')

class PostLikes(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    postId =  models.ForeignKey(UserPost, on_delete=models.CASCADE) 

    class Meta:
        db_table = "post_likes"

class PostComment(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    postId = models.ForeignKey(UserPost, on_delete=models.CASCADE) 
    commentText = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now())
    
    class Meta: 
        db_table = "post_comment"

