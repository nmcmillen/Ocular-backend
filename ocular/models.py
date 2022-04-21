from django.db import models

# Create your models here.
class User_Accounts(models.Model):
    email = models.CharField(null=False, max_length=255)
    password = models.CharField(null=False, max_length=255)
    name = models.CharField(null=False, max_length=255)
    avatar = models.CharField(null=False, max_length=255)
    number_of_posts = models.IntegerField(null=False, default=0)
    number_of_followers = models.IntegerField(null=False, default=0)
    number_of_following = models.IntegerField(null=False, default=0)

class Posts(models.Model):
    photos = models.ForeignKey(Photos, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    category = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User_Accounts, on_delete=models.CASCADE)
    number_of_likes = models.IntegerField(default=0)

class Post_Reactions(models.Model):
    # not sure if cascade should be the default on delete
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User_Accounts, on_delete=models.CASCADE)

class User_Notifications(models.Model):
    # post is referencing an image/gallery so maybe name should be different?
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User_Accounts, on_delete=models.CASCADE)

#need a user_following?

# this has both the follower's id and the user's id
class User_Followers(models.Model):
    follower = models.ForeignKey(User_Accounts, on_delete=models.CASCADE)
    user = models.ForeignKey(User_Accounts, on_delete=models.CASCADE)

class Post_Categories(models.Model):
    title = models.CharField(max_length=100)

class Photos(models.Model):
    images = models.ImageField(null=False)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)