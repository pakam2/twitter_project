from django import forms
from django.forms import ModelForm
from .models import Tweet



class TweetForm(ModelForm):
     class Meta:
         model = Tweet
         fields = ['content',]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
