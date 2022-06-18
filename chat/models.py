from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    
    username = models.CharField(max_length=100 , null = True)    
    text = models.CharField(max_length=1000 , null=True)