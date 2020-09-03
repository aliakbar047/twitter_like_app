from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class TweetForm(forms.ModelForm):
    class Meta:
        model = ThoughtTweet
        fields = ('tweet',)
        widgets = {
          'tweet': forms.Textarea(attrs={'rows':4, 'cols':40}),
        }
        labels = {
            'tweet': '',
        }
        help_texts = {
            'tweet': ('Write your Thoughts.'),
        }
        


    