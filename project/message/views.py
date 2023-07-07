from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LetterSerializer
from accounts.models import User
from .models import Letter
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import get_list_or_404


@api_view(['POST'])
def create_letter(request):
    user_email = request.data.get('user_email')
    content = request.data.get('content')

    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=400)

    data = {'user': user.id, 'content': content}
    serializer = LetterSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class LetterAPIView(APIView):
    model = Letter
    serializer_class = LetterSerializer

    def get(self, request, user_id):
        letters = get_list_or_404(Letter, user_id=user_id)
        serializer = self.serializer_class(letters, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        data = request.data
        data["user_id"] = user_id  # 추가: user_id를 주어진 user_id 값으로 지정합니다.
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)