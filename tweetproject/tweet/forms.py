from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from djnago.contrib.auth.models import user

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']


class userRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=user
        fields=('username','email','password1','password2')        