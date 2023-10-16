from django_filters.rest_framework import FilterSet
from . models import *

class BookFilter(FilterSet):
    class Meta:
        model = Book
        # fields = ['name','author','genre']
        fields = {'name':['startswith'],
                    'author':['startswith'],
                    'genre':['exact'],
                    'borrower':['isnull'],
                    'shelf':['exact']}