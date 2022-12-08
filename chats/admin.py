from django.contrib import admin
from chats.models import ChatModel, UserPost, Photo
# Register your models here.
admin.site.register(ChatModel)
admin.site.register(UserPost)
admin.site.register(Photo)
