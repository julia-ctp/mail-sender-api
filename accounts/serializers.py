from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import uuid


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "date_joined")
        read_only_fields = ("id", "date_joined")


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("email", "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data, username=str(uuid.uuid4()))
        user.set_password(password)
        user.save()

        return user


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"