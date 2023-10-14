from django.contrib import admin
from . models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'genre', 'shelf', 'borrower', 'date_borrowed', 'date_to_be_returned']
    search_fields = ['borrower__first_name','borrower__last_name','borrower__student_number','genre','name','author']
    list_per_page = 10
    autocomplete_fields = ['borrower']
    list_filter = ['genre','date_borrowed','date_to_be_returned']
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'occupation', 'student_number', 'financial_balance']
    search_fields = ['first_name', 'last_name','student_number']
    list_filter = ['occupation']
    list_per_page = 10
@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ['number', 'student', 'date_rented', 'date_expires', 'cost']
    autocomplete_fields = ['student']
    search_fields = ['student__first_name', 'student__last_name', 'student__student_number']
    list_filter = ['cost','date_rented']
    list_per_page = 10