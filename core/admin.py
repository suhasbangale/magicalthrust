from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, Jobpost, Startuppost

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Jobpost)
admin.site.register(Startuppost)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
