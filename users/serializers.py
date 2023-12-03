from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')
        

class ProfileSerializer(CustomUserSerializer):
    """
    Serializer class to serialize the user Profile model
    """
    class Meta:
        model = Profile
        fields = ('bookmarks', 'bio')


class ProfileAvatarSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize the avatar
    """
    class Meta:
        model = Profile
        fields = ('avatar',)