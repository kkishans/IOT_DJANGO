from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.TextField()
    email = models.EmailField(unique=True)
    objects = models.Manager()
    def __str__(self):
        return self.username

class Room(models.Model):
    
    room = models.CharField(max_length=30)
    email = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table = "room"
