from django.shortcuts import render
from django.contrib.auth import get_user_model
from chats.models import ChatModel
from django.contrib.auth.decorators import login_required
from .services import set_name_group
# Create your views here.


User = get_user_model()


def index(request):
    #дістаєм об'єкти користувача з бази данних
    users = User.objects.exclude(username=request.user.username)
    #рендерим головну сторінку чаму, передаючи параметром данні про користувача
    return render(request, 'chat\index.html', context={'users': users})

@login_required(login_url="/accounts/login/")
def chatPage(request, username):
    #дістаєм об'єкти користувача з бази данних
    user_obj = User.objects.get(username=username)
    #дістаєм об'єкти користувача з бази данних
    users = User.objects.exclude(username=request.user.username)
    #дістаємо з бази данних повідомлення за цим полем
    message_objs = ChatModel.objects.filter(thread_name=set_name_group())
    #рендеримо сторінку чату, передаючи параметрами користувачів та повідомлення
    return render(request, 'chat\chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})



