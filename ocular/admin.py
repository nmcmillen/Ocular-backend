from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(PostReaction)
admin.site.register(UserNotification)
admin.site.register(Follower)
admin.site.register(Photo)