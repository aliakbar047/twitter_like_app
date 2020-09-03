from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username


class ThoughtTweet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tweet = models.TextField(max_length=255)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)


    def __str__(self):
        return self.user.user.username

    def total_likes(self):
        total = self.likes.count()
        return total
