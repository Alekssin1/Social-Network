from django.contrib import admin
from our_post.models import UserPost, Photo, PostLikes
# Register your models here.
    
admin.site.register(UserPost)
admin.site.register(Photo)
admin.site.register(PostLikes)

    
    