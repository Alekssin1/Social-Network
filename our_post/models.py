from django.db import models
from datetime import datetime
from django.conf import settings

# модель, що відповідає за пости
class UserPost(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    createdAt = models.DateTimeField(default=datetime.now())
    content = models.ManyToManyField("Photo")

    class Meta: 
        db_table = "user_post"
        
# модель, що відповідає за фото до постів    
class Photo(models.Model):
    photo = models.FileField(upload_to='uploads/')

# модель, що відповідає за лайки до постів
class PostLikes(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    postId =  models.ForeignKey(UserPost, on_delete=models.CASCADE) 

    class Meta:
        db_table = "post_likes"

# модель, що відповідає за коментарі до постів
class PostComment(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    postId = models.ForeignKey(UserPost, on_delete=models.CASCADE) 
    commentText = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now())
    
    class Meta: 
        db_table = "post_comment"