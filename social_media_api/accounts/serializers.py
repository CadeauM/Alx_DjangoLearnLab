# Serializers are used to convert complex data types (like models) into JSON (a format that's easy to work with in APIs).
from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    token = serializers.CharField(read_only=True)
    class Meta: 
        model = User
        fields = ('username', 'email', 'password', 'token')
        def create(self, validated_data): # Create a new user using the validated data
            user = User.objects.create_user( username=validated_data['username'], email=validated_data.get('email'), password=validated_data['password'] ) # Generate a token for the user 
            token = Token.objects.create(user=user) 
            user.token = token.key

            # Generate a token for the user
            token = Token.objects.create(user=user)
            user.token = token.key
            return user


