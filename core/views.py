from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *
from .filters import *
from .pagination import *
class LibrarianViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    filterset_class = LibrarianFilter
    pagination_class = DefaultPagination

class ShiftViewSet(ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    pagination_class = DefaultPagination
    filterset_class = ShiftFilter
