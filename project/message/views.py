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

    def post(self, request, user_id): #post 메서드 정의. #request객체와 user_id의 인자를 받음
        data = request.data
        data["user_id"] = user_id  # 추가: user_id를 주어진 user_id 값으로 지정.
        serializer = self.serializer_class(data=data) #data를 인코딩하거나 디코딩할 수 있도록 serializer 객체를 생성.
        if serializer.is_valid():
            serializer.save() #유효한 직렬화 객체를 데이터베이스에 저장.
            return Response(serializer.data, status=status.HTTP_201_CREATED) #저장된 객체의 데이터를 반환, 201를 포함하는 Response 객체 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #직렬화 객체가 유효하지 않은 경우, 발생한 오류를 반환하고 상태 코드 400를 포함하는 Response 객체를 반환
