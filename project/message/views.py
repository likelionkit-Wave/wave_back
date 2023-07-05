from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LetterSerializer
from accounts.models import User

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
