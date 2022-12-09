from django.shortcuts import render
from django.contrib.auth import get_user_model
from chats.models import ChatModel
from django.contrib.auth.decorators import login_required
# Create your views here.


User = get_user_model()


def index(request):
    #дістаєм об'єкти користувача з бази данних
    users = User.objects.exclude(username=request.user.username)
    #рендерим головну сторінку чаму, передаючи параметром данні про користувача
    return render(request, 'index.html', context={'users': users})




@login_required(login_url="/accounts/login/")
def chatPage(request, username):
    #дістаєм об'єкти користувача з бази данних
    user_obj = User.objects.get(username=username)
    #дістаєм об'єкти користувача з бази данних
    users = User.objects.exclude(username=request.user.username)

    #даємо назву групі, від більшого айді користувача до меншого
    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    #дістаємо з бази данних повідомлення за цим полем
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    #рендеримо сторінку чату, передаючи параметрами користувачів та повідомлення
    return render(request, 'chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})



