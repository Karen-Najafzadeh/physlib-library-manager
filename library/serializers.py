from rest_framework.serializers import ModelSerializer
from .models import *

class BookSerializerSimple(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'genre', 'shelf', 'number']

class BookSerializerDetailed(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'