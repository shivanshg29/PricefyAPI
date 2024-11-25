from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Link
from rest_framework_simplejwt.tokens import RefreshToken

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)  # Include user links

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'links']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
