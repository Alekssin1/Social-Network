import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chats.models import ChatModel
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class PersonalChatConsumer(AsyncWebsocketConsumer):
    # функція що проводить конект до веб сокетів
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        # називаємо групу від більшого айді користувача до меншого
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        # створюємо групу
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.set_online_user(my_id, True)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        # дістаємо json з js
        data = json.loads(text_data)
        message = data['message']
        
        # перевіряємо повідомлення на пустоту
        if message.strip() != "": 
            username = data['username']
            myTime = datetime.now()
        
            # перевіряємо чи є в повідомленні голосове
            if data['base64'] == "1":
                await self.save_message(username, self.room_group_name, message, myTime, True)
            else:
                await self.save_message(username, self.room_group_name, message, myTime)
            # відправка даних в chat_message 
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'timestamp': myTime,
                    'base64': data['base64'],
                }
            )


    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        base64 = event['base64']

        # відправка даних в json, для подальшої роботи в js
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'base64': base64,
        }))

    async def disconnect(self, code):
        my_id = self.scope['user'].id
        await self.set_online_user(my_id, False)
        await self.set_last_time_online(my_id)
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # збереження повідомлення в базі даних
    @database_sync_to_async
    def save_message(self, username, thread_name, message, myTime, base=False):
        ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name, timestamp=myTime, base64=base)
      
    @database_sync_to_async  
    def set_online_user(self, id, data):
        User.objects.filter(id=id).update(is_online=data)
        
    @database_sync_to_async  
    def set_last_time_online(self, id):
        User.objects.filter(id=id).update(last_time_online=datetime.now())
        