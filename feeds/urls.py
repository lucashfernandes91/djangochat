from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login_user, name='login'),
	path('signout/', views.signout, name='signout'),
	path('signup/', views.signup, name='signup'),
	path('signup_success/', views.signup_success, name='signup_success'), # pagina nao usada, verificar
	path('explore/', views.explore, name='explore'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('profile/<str:username>/edit/', views.profile_settings, name='profile_settings'),    
	path('profile/<str:username>/followers/', views.followers, name='followers'),
	path('profile/<str:username>/following/', views.following, name='following'), 
	path('notifications/', views.notifications, name='notifications'),
	path('new_chat/', views.new_chat, name='new_chat'), # alterar
	path('new_chat/<str:username>/', views.new_chat_create, name='new_chat_create'),	# alterar
	path('post/<int:pk>/', views.post, name='post'),
	path('post/<int:pk>/likes/', views.likes, name='likes'),
	path('post/', views.post_picture, name='post_picture'),	   
	path('like/', views.add_like, name='like'),
	path('comment/', views.add_comment, name='comment'),
	path('follow_toggle/', views.follow_toggle, name='follow_toggle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)