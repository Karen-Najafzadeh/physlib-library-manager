from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from django_filters import rest_framework as filter
from .models import *
from .serializers import *
from .filters import *
from .pagination import DefaultPagination

class BookViewset(ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Book.objects.all()
    filterset_class = BookFilter

    def get_serializer_class(self):
        print(self.action,'\n\n\n\n')
        if self.action in ['retrieve','update','partial_update']:
            return BookSerializerDetailed
        else:
            return BookSerializerSimple

class MemberViewset(ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filterset_class = MemberFilter

class LockerViewset(ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    filterset_class = LockerFilter