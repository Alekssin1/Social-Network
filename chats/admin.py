from django.contrib import admin
from chats.models import ChatModel

# регісрація в адмін панелі моделей чату, посту та фотографії до посту
admin.site.register(ChatModel)

