from django_filters.rest_framework import FilterSet
from .models import *

class IncomeFilter(FilterSet):
    class Meta:
        model = Income
        fields = {
            'date':['lt', 'gt'],
            'title':['icontains'],
            'type':['exact'],
        }