from rest_framework.serializers import ModelSerializer
from .models import *

class TreasurySerializer(ModelSerializer):
    class Meta:
        model = Treasury
        fields = '__all__'

class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
