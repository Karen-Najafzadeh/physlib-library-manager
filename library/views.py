from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
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

    @action(detail=True)
    def member_books(*args, **kwargs):
        queryset = Book.objects.filter(borrower_id = kwargs['pk'])
        serializer = BookSerializerSimple(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def member_locker(*args, **kwargs):
        queryset = get_object_or_404(Locker, student_id = kwargs['pk'])
        serializer = LockerSerializerSimple(queryset)
        return Response(serializer.data)

class LockerViewset(ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    filterset_class = LockerFilter