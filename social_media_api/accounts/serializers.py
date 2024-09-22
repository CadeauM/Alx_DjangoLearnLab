# Serializers are used to convert complex data types (like models) into JSON (a format that's easy to work with in APIs).
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
