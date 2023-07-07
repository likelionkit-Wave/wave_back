from rest_framework import serializers
from .models import Letter

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        
        fields = ['id', 'title','user', 'content', 'is_read', 'writer','send_date',]