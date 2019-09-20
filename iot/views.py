from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib.auth.views import LoginView,LogoutView
from .models import User
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
