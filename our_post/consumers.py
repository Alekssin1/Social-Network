import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chats.models import PostComment, UserPost
from django.contrib.auth.models import User
from datetime import datetime


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = int(self.scope['user'].id)
        self.room_group_name = str(self.scope['url_route']['kwargs']['id'])
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None):
        data = json.loads(text_data)
        comment = data['comment']

        if comment.strip() != "":
            username = data['username']
            myTime = datetime.now()
            # print(username, type(username))
            usernames = await self.get_user(username)
            id = await self.get_post(int(self.room_group_name))
            print("-"*30, usernames)
            await self.save_comment(usernames, id, comment, myTime)
            user = self.get_username(usernames)
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

        await self.send(text_data=json.dumps({
            'comment': comment,
            'username': username,
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_comment(self, id_user, id_post, comment, myTime):
        PostComment.objects.create(
            userId=id_user, postId=id_post, commentText=comment, createdAt=myTime)

    @database_sync_to_async
    def get_user(self, username):
        return User.objects.get(id=username)

    @database_sync_to_async
    def get_post(self, id):
        return UserPost.objects.get(id=id)

    # @database_sync_to_async
    def get_username(self, obj):
        return getattr(obj, 'username')
