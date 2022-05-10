from django.shortcuts import render
from .models import User, Tag, Post, PostReaction, PostMessage, Follower, Photo
from .serializers import (
    UserSerializer,
    TagSerializer,
    PostSerializer,
    PostReactionSerializer,
    PostMessageSerializer,
    FollowerSerializer,
    PhotoSerializer
)
from rest_framework import viewsets, permissions, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.http import HttpResponse  # new
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

# Trying for photo upload
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.parsers import JSONParser


# Create your views here.

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('username')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'username']
    # turned this on for view name on frontend when signed in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #new changed to view user data to build profile page


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['hashtag']


class PostViewSet(viewsets.ModelViewSet):
    # shows each post by most recent by using "-" with created_date
    queryset = Post.objects.order_by('-created_date')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['created_by__username', 'hashtag__hashtag']
    filterset_fields = ['created_by', 'hashtag__hashtag']

    def create(self, request):
        # Grab user id and lookup the user.
        user_id = request.data.pop('created_by')
        user = User.objects.get(pk=int(user_id[0])) ##THIS WORKS JUST (user_id) does not
        file = request.data['image']
        request.data.pop('image')
        description = request.data.pop('description')
        # user = User.objects.get(user_id)
        # print(uploaded_image)
        # file = request.FILES.get('uploaded_image')
        # print(request.data['description'])
        # print(type(request.data['description']))
        # return
        print(file.content_type)
        if file.content_type == 'image/jpeg' or 'image/png':
            post = Post.objects.create(created_by=user, description=description, **request.data)
            photo = Photo()
            photo.post = post
            photo.images.save(
                file.name,
                file,
            )
            photo.save()
            print(file.name)

        # Take Photos out of request.data to create the photos.
        # photo = Photo.object.create(images=uploaded_image, post=post)
            return HttpResponse('Created successfully')


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
    queryset = Photo.objects.order_by('-id')
    serializer_class = PhotoSerializer
