from rest_framework.serializers import ModelSerializer
from .models import *

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'