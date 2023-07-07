from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LetterSerializer
from accounts.models import User
from .models import Letter

#편지쓰기
@api_view(['POST'])
def create_letter(request):
    #사용자 계정, 제목, 내용, 작성자, 날짜
    user_email = request.data.get('user_email')
    title = request.data.get('title')
    content = request.data.get('content')
    writer = request.data.get('writer')

    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=400)

    data = {'user': user.id, 'content': content, 'title':title, 'writer':writer}
    serializer = LetterSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#편지보기
@api_view(['GET'])
def detail_letter(request, letter_id):
    letter = Letter.objects.get(pk=letter_id)
    letter.is_read = True  # is_read 필드 값을 True로 설정
    letter.save()  # 변경된 값을 데이터베이스에 저장

    serializer = LetterSerializer(letter)
    return Response(serializer.data)

#편지삭제
@api_view(['DELETE'])
def delete_letter(request, letter_id):
    try:
        letter = Letter.objects.get(pk=letter_id)
        letter.delete()
        return Response(status=204)
    except Letter.DoesNotExist:
        return Response({'error': 'Letter not found'}, status=404)