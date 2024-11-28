from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'email', 'password']
    
    def create(self,validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'