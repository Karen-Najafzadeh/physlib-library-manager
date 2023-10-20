from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework.generics import CreateAPIView,ListAPIView
from django_filters import rest_framework as filter
from .models import *
from finance.models import Income
from finance.serializers import IncomeSerializer
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

    @action(detail=True)
    def book_now(self, *args, **kwargs):
        return redirect (f"http://127.0.0.1:8000/library/lockers/{self.kwargs['pk']}/booking/")

class Booking(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=True)
    def book_for_the_current_member(self, *args, **kwargs):
        return redirect(f"http://127.0.0.1:8000/library/lockers/{self.kwargs['locker_pk']}/booking/{self.kwargs['pk']}/pricing/")
        # print(f'initial {self.kwargs}\n\n{kwargs}\n\n{args}')
        locker = Locker.objects.get(pk=self.kwargs['locker_pk'])
        student_id = Member.objects.get(pk = self.kwargs['pk'])
        print(f'queries {student_id.pk}\n\n {locker.pk} and {locker.student}')
        locker.student = student_id
        locker.save()
        # print(f'locker {locker.student}')
        return Response(f'{locker.pk} {locker.cost} {locker.student}')

class Pricing(ModelViewSet):
    queryset = Income.objects.all()
    def list(self, *args, **kwargs):
        return Response('create a new income object')
    def create(self,request, *args, **kwargs):
        locker = Locker.objects.get(pk=self.kwargs['locker_pk'])
        student_id = Member.objects.get(pk = self.kwargs['new_income_pk'])
        locker.student = student_id
        locker.save()
        serializer = IncomeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    serializer_class = IncomeSerializer