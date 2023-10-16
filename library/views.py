from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from django_filters import rest_framework as filter
from .models import *
from .serializers import *
from .filters import *

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    filterset_class = BookFilter

    def get_serializer_class(self):
        print(self.action,'\n\n\n\n')
        if self.action in ['retrieve','update','partial_update']:
            return BookSerializerDetailed
        else:
            return BookSerializerSimple