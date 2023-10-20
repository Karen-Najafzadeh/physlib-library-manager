from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . models import * 

class LibrarianSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Librarian
        fields = ['student_number', 'phone_number', 'user']

class ShiftSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'