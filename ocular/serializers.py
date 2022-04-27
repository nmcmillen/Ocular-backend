from .models import User, Tag, Post, PostReaction, PostMessage, Follower, Photo
from rest_framework import serializers

### IMPORTANT: May need to change gitpod link each time a new workspace is opened ###
BASE_API_URL = 'https://8000-nmcmillen-ocularbackend-sm1tv8tjiev.ws-us42.gitpod.io'

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = User
        fields = '__all__'

    # changes the photo link for Django REST to be viewable when clicked
    def get_image_url(self, obj):
        if obj.avatar:
            return BASE_API_URL + obj.avatar.url


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField('get_images')
    # photos = serializers.SerializerMethodField('get_image_url')
    hashtag = serializers.StringRelatedField(many=True)
    # photos = serializers.StringRelatedField(many=True) #returns "Photo Object (7)"
    created_by = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    # **Not sure why this doesn't work**
    # photos = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='images'
    # )

    class Meta:
        model = Post
        fields = (
            'description',
            'hashtag',
            'created_date',
            'updated_date',
            'created_by',
            'number_of_likes',
            'photos'
        )

    # def get_image_url(self, obj):
    #     if obj.photos:
    #         return BASE_API_URL + obj.photos.url


class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = '__all__'


class PostMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMessage
        fields = '__all__'


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'
        

class PhotoSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Photo
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.images:
            return BASE_API_URL + obj.images.url