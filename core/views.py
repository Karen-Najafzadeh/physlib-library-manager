from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .filters import *
from .pagination import *
class LibrarianViewSet(ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    filterset_class = LibrarianFilter
    pagination_class = DefaultPagination