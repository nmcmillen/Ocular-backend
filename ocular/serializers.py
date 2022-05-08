from .models import User, Tag, Post, PostReaction, PostMessage, Follower, Photo
from rest_framework import serializers
from django.utils.timezone import now
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #new

### IMPORTANT: May need to change gitpod link each time a new workspace is opened ###
BASE_API_URL = 'https://8000-nmcmillen-ocularbackend-sm1tv8tjiev.ws-us44.gitpod.io'

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    # password = serializers.CharField(min_length=8, write_only=True) #new

    avatar = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = User
        fields = (
            'id',
            'avatar',
            'username',
            'first_name',
            'last_name',
            'bio',
            'email',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data): #all below to return new
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    # changes the photo link for Django REST to be viewable when clicked
    def get_image_url(self, obj):
        if obj.avatar:
            return BASE_API_URL + obj.avatar.url


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class PhotoSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Photo
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.images:
            return BASE_API_URL + obj.images.url

class PostSerializer(serializers.ModelSerializer):
    hashtag = serializers.StringRelatedField(many=True) #turns hashtag to readable string
    photos = PhotoSerializer(read_only=True, many=True) #from Photo in models.py gets images related to post
    created_by = UserSerializer(read_only=True)
    created_date = serializers.SerializerMethodField('change_time_format')

    # since_date = serializers.SerializerMethodField('days_since')

    class Meta:
        model = Post
        fields = (
            'id',
            'description',
            'hashtag',
            'created_date',
            'updated_date',
            'created_by',
            'number_of_likes',
            'photos'
        )

    # def create(self, validated_data):
    #     # Grab user id and lookup the user.
    #     user_id = validated_data.pop('created_by')
    #     # user = User.objects.get(user_id)
    #     user = User.objects.get(pk=int(user_id[0])) ##THIS WORKS JUST (user_id) does not
    #     file = validated_data['image']
    #     validated_data.pop('image')
    #     # print(uploaded_image)
    #     # file = validated_data.FILES.get('uploaded_image')
    #     description = validated_data.pop('description')
    #     # print(validated_data.data['description'])
    #     # print(type(validated_data.data['description']))
    #     # return
    #     print(file.content_type)
    #     if file.content_type == 'image/jpeg' or 'image/png':
    #         post = Post.objects.create(created_by=user, description=description, **validated_data)
    #         photo = Photo()
    #         photo.post = post
    #         photo.images.save(
    #             file.name,
    #             file,
    #         )
    #         photo.save()
    #         print(file.name)

    #     # Take Photos out of validated_data.data to create the photos.
    #     # photo = Photo.object.create(images=uploaded_image, post=post)
    #         return HttpResponse('Created successfully')

    # https://www.geeksforgeeks.org/how-to-format-date-using-strftime-in-python/
    def change_time_format(self,obj):
        return obj.created_date.strftime("%b %d, %Y")
    
    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    # def days_since(self, obj):
    #     if obj.since_date:
    #         return (now() - obj.created_date).days

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
        

