from django.shortcuts import render
from django.contrib.auth import get_user_model
from chats.models import ChatModel
from django.contrib.auth.decorators import login_required
from .services import set_name_group
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

User = get_user_model()

class Base_chat(ListView):
    model = User
    template_name = 'chat\index.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        return User.objects.exclude(username=self.request.user.username).select_related('avatar')

class Chat_page(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'chat\chat.html'
    pk_url_kwarg = 'username'
    context_object_name = 'users'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        return User.objects.exclude(username=self.request.user.username).select_related('avatar')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_obj = User.objects.filter(username=self.kwargs.get("username")).select_related('avatar').first()
        context['user'] = user_obj
        context['messages'] = ChatModel.objects.filter(thread_name=set_name_group(self.request, user_obj))
        return context