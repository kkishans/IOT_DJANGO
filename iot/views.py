from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User,Room
# Create your views here.

def home(request):
    # template = loader.get_template('welcome.html')
    users = User.objects.all()
    return render(request,'welcome.html',{'users':users})
def dashboard(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return render(request,'dashboard.html',{'users':users})
    else:
        return HttpResponseRedirect("login")

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("dashboard")
    else:
      return HttpResponseRedirect("login")



class RoomList(ListView): 
    model = Room
    fields = '__all__'


class RoomCreate(CreateView): 
    model = Room
    fields = '__all__'
    

class RoomUpdate(UpdateView): 
    model = Room
    fields = '__all__'


class RoomDelete(DeleteView): 
    model = Room
    fields = '__all__'