from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request,'index.html',{'users':users})
    
def home(request):
    # template = loader.get_template('welcome.html')
    users = User.objects.all()
    return render(request,'welcome.html',{'users':users})
def dashbord(request):
    # template = loader.get_template('welcome.html')
    return render(request,'dashboard.html',{})