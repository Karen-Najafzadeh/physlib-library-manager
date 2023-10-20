from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as UCS
from . models import * 

class UserCreateSerializer(UCS):
    class Meta(UCS.Meta):
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
class LibrarianSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Librarian
        fields = ['student_number', 'phone_number', 'user']

class ShiftSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'