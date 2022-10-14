from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from user.models import TOKENS
from .models import Todo
from django.contrib.auth.models import User

class TodoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title" , "description" , "start_date" , "end_date" , "user"]

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOKENS
        fields = ["token" , "user"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username" , "password"]


