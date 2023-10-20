from django_filters.rest_framework import FilterSet
from .models import *

class LibrarianFilter(FilterSet):
    class Meta:
        model = Librarian
        fields = {
            'student_number':['exact']
        }

class ShiftFilter(FilterSet):
    class Meta:
        model = Shift
        fields = {
            'day':['exact'],
            'librarian':['exact']
        }