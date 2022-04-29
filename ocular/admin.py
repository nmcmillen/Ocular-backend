from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model #new
from django.contrib.auth.admin import UserAdmin #new

# Register your models here.
# admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(PostReaction)
admin.site.register(PostMessage)
admin.site.register(Follower)
admin.site.register(Photo)
admin.site.register(User, UserAdmin) #new, may remove User since it's already added above I think
