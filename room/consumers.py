import json

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room']

		await self.channel_layer.group_add(
			self.room_name,
            self.channel_name

		)

		await self.accept()

	async def disconnect(self):
		await self.channel_layer.group_discard(
			self.room_name,
			self.channel_name
		)

	# Receive message from WebSocket
	async def receive(self, text_data):
		data = json.loads(text_data)
		message = data['message']
		username = data['username']
		room = data['room']
		
		await self.save_message(username, room, message)

		# Send message to room group
		await self.channel_layer.group_send(
			self.room_name,
			{
				'type': 'chat_message',
				'message': message,
				'username': username
			}
		)

	# Receive message from room group
	async def chat_message(self, event):
		message = event['message']
		username = event['username']

		# Send message to WebSocket
		await self.send(text_data=json.dumps({
			'message': message,
			'username': username
		}))

	@sync_to_async
	def save_message(self, user, room, message):
		print(room)
		room = Room.objects.get(label=room)
		user = User.objects.get(username=user)
		#message = Message.objects.get(text=message)

		Message.objects.create(sender=user, room=room, text=message)