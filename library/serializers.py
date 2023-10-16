from rest_framework import serializers
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

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'student_number']
class LockerSerializer(ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:

        model = Locker
        fields = ['number','cost','student']