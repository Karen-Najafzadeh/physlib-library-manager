from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from django_filters import rest_framework as filter
from .models import *
from .serializers import *
from .filters import *

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter