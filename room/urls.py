from django.urls import path

from . import views

urlpatterns = [
	path('', views.inbox, name='inbox'),
	path('<str:label>/', views.chat, name='chat'),
	#path('<slug:slug>/', views.room, name='room'),
]