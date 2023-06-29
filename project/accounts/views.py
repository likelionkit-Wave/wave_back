from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from accounts.serializers import UserSerializer
from accounts.models import User

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request):
        response = super().post(request)
        token_key = response.data['token']
        token = Token.objects.get(key=token_key)
        response.data['token_user_id'] = token.user_id
        # 추가 필요한 경우 다른 정보도 전달할 수 있습니다.
        return response