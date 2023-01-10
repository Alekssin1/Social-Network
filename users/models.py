from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class AvatarUser(models.Model):
    avatar = models.FileField(upload_to='uploads/avatar/')
    default = models.BooleanField(default=False)
    
    @staticmethod
    def defaultImg():
        if AvatarUser.objects.filter(default=True).exists():
            return AvatarUser.objects.get(default=True)
        defaultAvatar = AvatarUser(avatar='static/default/avatar/dp.png', default=True)
        defaultAvatar.save()
        return defaultAvatar
    
class User(AbstractUser):
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    avatar = models.ForeignKey(AvatarUser, on_delete=models.CASCADE, default=AvatarUser.defaultImg)


    def __str__(self):
          return f"{self.username}"
      
    def getExcludeObjects(self):
        return reverse('chat', kwargs={'username': self.username})
    
    def getPkFollowToggle(self):
        return reverse('followToggle', kwargs={'username': self.username})
    
    def getUsernameProfile(self):
        return reverse('profile', kwargs={'username': self.username})
    
