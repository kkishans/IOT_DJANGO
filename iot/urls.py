from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .models import Room

urlpatterns = [
    path('' ,views.index),
    path('logout',LogoutView.as_view(template_name= "logout.html")),
    path('login', LoginView.as_view(template_name='index.html')),
    path('home' ,views.home),
    path('users' ,views.getData),
    path('dashboard' ,views.dashboard,name="Dashboard"),
    path('rooms', views.RoomList.as_view(), name='room_list'),
    path('add', views.RoomCreate.as_view(model=Room, success_url="/iot/rooms"), name='room_create'),
    path('update/<int:pk>', views.RoomUpdate.as_view(model=Room, success_url="/iot/rooms"), name='room_update'),
    path('delete/<int:pk>', views.RoomDelete.as_view(model=Room, success_url="/iot/rooms"), name='room_delete'),

]