from django.db import models
from datetime import datetime
from django.conf import settings
from django.urls import reverse

# модель, що відповідає за пости
class UserPost(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    createdAt = models.DateTimeField(default=datetime.now())
    content = models.ManyToManyField("Photo")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="collected_votes")
    comments = models.ManyToManyField("PostComment", blank=True,)

    class Meta: 
        db_table = "user_post"
        
    def get_absolute_url(self):
        return reverse('comments', kwargs={'post_id': self.pk})
    
    def get_pk_for_like(self):
        return reverse('like_post', kwargs={'id': self.pk})
        
# модель, що відповідає за фото до постів    
class Photo(models.Model):
    photo = models.FileField(upload_to='uploads/')

# модель, що відповідає за коментарі до постів
class PostComment(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    commentText = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now())
    
    class Meta: 
        db_table = "post_comment"