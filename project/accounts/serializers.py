from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.get('username')
        email = validated_data.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        return user