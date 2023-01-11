"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from chats.views import index, chatPage
from our_post.views import comments, posts, like_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # адмін панель
    path('admin/', admin.site.urls),
    
    # сторінка початкового чату
    path('', index, name='home'),
    
    # сторінка з можливістю зараєструватися, вийти з акаунту або стоворити його
    path('profile/', include('django.contrib.auth.urls')),
    
    path('profile/', include('users.urls')),
    
    #сторінка з всіма постами
    path('post/', include('our_post.urls')),
    
    # сторінка чату з користувачем
    path('<username>/', chatPage, name='chat'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # значення для завантаження медіа файлів(картинок до посту)
