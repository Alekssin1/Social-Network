from django.contrib import admin
from chats.models import ChatModel, UserPost, Photo
# Register your models here.

# регісрація в адмін панелі моделей чату, посту та фотографії до посту
admin.site.register(ChatModel)
admin.site.register(UserPost)
admin.site.register(Photo)
