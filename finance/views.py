from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .filters import *

class TreasuryViewSet(ModelViewSet):
    queryset = Treasury.objects.all()
    serializer_class = TreasurySerializer

class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    filterset_class = IncomeFilter
class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer