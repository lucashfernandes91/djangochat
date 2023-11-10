from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Room(models.Model):
	label = models.SlugField(unique=True)
	receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
	sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)

	def get_last_message(self):
		message = Message.objects.filter(room=self).last()
		return message.text if message else ""

	def get_last_message_timestamp(self):
		message = Message.objects.filter(room=self).last()
		return message.timestamp if message else ""

	def __str__(self):
		return self.label
	

class Message(models.Model):
	room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
	sender = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	timestamp = models.DateTimeField(default=datetime.now, db_index=True)

	def __str__(self):
		return self.text + " S:" + self.sender.username

"""class Room(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)"""


"""class Message(models.Model):
	room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
	content = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('date_added',)"""