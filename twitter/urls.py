from django.urls import path
from .views import *


urlpatterns = [
    path('', ThoughtSharing.as_view(), name = 'tweet'),
    path('tweet_like/<int:pk>', likeTweet, name = 'tweet_like'),
]