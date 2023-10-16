from django_filters.rest_framework import FilterSet
from . models import *

class BookFilter(FilterSet):
    class Meta:
        model = Book
        # fields = ['name','author','genre']
        fields = {'name':['startswith'],
                    'author':['startswith'],
                    'borrower':['isnull'],
                    'genre':['exact'],
                    'shelf':['exact']}