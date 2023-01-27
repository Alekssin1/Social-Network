import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chats.consumers import PersonalChatConsumer
from our_post.consumers import CommentConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

application = get_asgi_application()

# записуємо url для різних websocket
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
            path('ws/comment/<int:id>/', CommentConsumer.as_asgi()),
        ])
    )
})
