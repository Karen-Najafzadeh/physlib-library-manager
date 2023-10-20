from django_filters.rest_framework import FilterSet
from .models import *

class LibrarianFilter(FilterSet):
    class Meta:
        model = Librarian
        fields = {
            'student_number':['exact']
        }