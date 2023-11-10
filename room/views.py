from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

from .models import Room, Message

@login_required
def inbox(request):
	user = request.user
	rooms = Room.objects.filter(Q(receiver=user) | Q(sender=user))
	context = {
		'rooms': rooms
	}
	return render(request, 'room/inbox.html', context)

@login_required
def chat(request, label):
	user = request.user
	room = Room.objects.get(label=label)
	messages = Message.objects.filter(room=room)[0:25]
	return render(request, 'room/room.html', {'room': room,
										   	'messages': messages,
											'user': user})

	# user = request.user
	# room = Room.objects.get(label=label)
	# messages = reversed(room.messages.order_by('-timestamp')[:50])

	# return render(request, 'feeds/chat.html', {
	# 	'room': room,
	# 	'messages': messages
	# })