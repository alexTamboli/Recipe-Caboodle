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