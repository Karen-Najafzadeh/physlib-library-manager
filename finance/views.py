from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class TreasuryViewSet(ModelViewSet):
    queryset = Treasury.objects.all()
    serializer_class = TreasurySerializer