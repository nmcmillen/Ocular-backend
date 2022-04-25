from django.shortcuts import render
from .models import User, Tag, Post, PostReaction, PostMessage, Follower, Photo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, TagSerializer, PostSerializer, PostReactionSerializer, PostMessageSerializer, FollowerSerializer, PhotoSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permission.isAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostReactionViewSet(viewsets.ModelViewSet):
    queryset = PostReaction.objects.all()
    serializer_class = PostReactionSerializer


class PostMessageViewSet(viewsets.ModelViewSet):
    queryset = PostMessage.objects.all()
    serializer_class = PostMessageSerializer


class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
