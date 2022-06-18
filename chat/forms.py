from dataclasses import field
from django import forms 
from .models import  Message
from django.contrib.auth.models import User 

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username" , "first_name" , "last_name" , "email" , "password"]


class MessageForm(forms.Form):
    username = forms.CharField(max_length=100)
    text = forms.CharField(max_length=100)