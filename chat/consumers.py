import json

from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from channels.generic.websocket import WebsocketConsumer

from chat.models import Message


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        """
        Join channel group by chatname.
        """
        self.group_name = 'chat_{0}'.format(self.scope['url_route']['kwargs']['chatname'])

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )

        self.accept()

    def disconnect(self, close_code):
        """
        Leave channel by group name.
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        """
        Receive message from websocket and send message to channel group.
        """
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        message = text_data_json['message']

        # Store message.
        receiver = User.objects.get(
            username=self.group_name.replace('chat_', '')
                                    .replace(self.scope['user'].username, '')
                                    .replace('-', ''))
        Message(sender=self.scope['user'], receiver=receiver, text=message).save()

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message,
            }
        )

    def chat_message(self, event):
        """
        Receive message from channel group and send message to websocket.
        """
        self.send(text_data=json.dumps({
            'username': event['username'],
            'message': event['message'],
        }))
