from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings #from how to extend django user model article option 4

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField()
    # number_of_posts = models.IntegerField(null=False, default=0)
    # number_of_followers = models.IntegerField(null=False, default=0)
    # number_of_following = models.IntegerField(null=False, default=0)

class Tags(models.Model):
    hashtag = models.CharField(max_length=100)

class Posts(models.Model):
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Tags, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_of_likes = models.IntegerField(default=0)

class PostReactions(models.Model):
    # not sure if cascade should be the default on delete
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class UserNotifications(models.Model):
    # post is referencing an image/gallery so maybe name should be different?
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#need a user_following?

# this has both the follower's id and the user's id
class Followers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Photos(models.Model):
    images = models.ImageField(null=False)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    category = models.ForeignKey(Tags, on_delete=models.CASCADE)