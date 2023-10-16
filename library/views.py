from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import *
from .serializers import *

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer