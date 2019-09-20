from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('' ,views.index),
    path('logout',LogoutView.as_view(template_name= "logout.html")),
    path('login', LoginView.as_view(template_name='index.html')),
    path('home' ,views.home),
    path('dashboard' ,views.dashboard),
]