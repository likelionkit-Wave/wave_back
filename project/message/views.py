from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Letter
from .serializers import LetterSerializer

# 편지보기
@api_view(['GET'])
def read_letter_detail(request, letter_id):
    letter = Letter.objects.get(pk=letter_id)
    serializer = LetterSerializer(letter)
    return Response(serializer.data)

# 편지삭제
@api_view(['DELETE'])
def delete_letter(request, letter_id):
    letter = Letter.objects.get(pk=letter_id)
    letter.delete()
    return Response(status=204)

# 편지쓰기
@api_view(['POST'])
def create_letter(request):
    serializer = LetterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)