from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )


    def __str__(self):
          return f"{self.username}"
      
    def getExcludeObjects(self):
        return reverse('chat', kwargs={'username': self.username})
    
    def getPkFollowToggle(self):
        return reverse('followToggle', kwargs={'username': self.username})
      