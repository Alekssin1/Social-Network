import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from our_post.models import PostComment, UserPost
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = int(self.scope['user'].id)
        self.room_group_name = str(self.scope['url_route']['kwargs']['id'])
        # створюємо групу
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None):
        data = json.loads(text_data)
        comment = data['comment']

        # перевірка на пустоту вводу
        if comment.strip() != "":
            username = data['username']
            myTime = datetime.now()
           
            usernames = await self.get_user(username)
            id = await self.get_post(int(self.room_group_name))
   
            # зберігання даних в базі
            
            await self.save_comment(usernames, id, comment, myTime)
            user = self.get_username(usernames)
            
            # відправка даних в comment_message
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'comment_message',
                    'comment': comment,
                    'username': user,
                    'timestamp': myTime,
                }
            )

    async def comment_message(self, event):
        comment = event['comment']
        username = event['username']

        # відправка даних в json для подальшої роботи в js
        await self.send(text_data=json.dumps({
            'comment': comment,
            'username': username,
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # зберігає коментар в базі
    @database_sync_to_async
    def save_comment(self, id_user, id_post, comment, myTime):
        comment = PostComment(userId=id_user, commentText=comment, createdAt=myTime)
        comment.save()
        id_post.comments.add(comment)
        id_post.save()

    # отримує об'єкти користувачів з бази 
    @database_sync_to_async
    def get_user(self, username):
        return User.objects.get(id=username)

    # отримує об'єкти постів з бази 
    @database_sync_to_async
    def get_post(self, id):
        return UserPost.objects.get(id=id)

    # отримує поле username з об'єкта
    def get_username(self, obj):
        return getattr(obj, 'username')
