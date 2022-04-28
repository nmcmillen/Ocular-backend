from django.shortcuts import render
from .models import User, Tag, Post, PostReaction, PostMessage, Follower, Photo
from .serializers import UserSerializer, TagSerializer, PostSerializer, PostReactionSerializer, PostMessageSerializer, FollowerSerializer, PhotoSerializer
from rest_framework import viewsets, permissions, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'username']
    # permission_classes = [permission.isAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['hashtag']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_date') #shows each post by most recent by using "-" with created_date
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['created_by__username', 'hashtag__hashtag']
    filterset_fields = ['created_by', 'hashtag']


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
