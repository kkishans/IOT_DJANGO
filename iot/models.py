from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.TextField()
    email = models.EmailField()
    objects = models.Manager()
    def __str__(self):
        return self.username
