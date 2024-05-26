from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import Client
from project.models import Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
class ClientSerializer(serializers.ModelSerializer):
    
    createdBy = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    createdBy = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
