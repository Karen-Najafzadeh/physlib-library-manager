from django_filters.rest_framework import FilterSet
from . models import *

class BookFilter(FilterSet):
    class Meta:
        model = Book
        # fields = ['name','author','genre']
        fields={'name':['startswith'],
                'author':['startswith'],
                'borrower':['isnull'],
                'genre':['exact'],
                'shelf':['exact']}

class MemberFilter(FilterSet):
    class Meta:
        model = Member
        fields={'student_number':['exact'],
                'occupation':['exact']}
        
class LockerFilter(FilterSet):
    class Meta:
        model = Locker
        fields={'student__student_number':['exact'],
                'student':['isnull'],}