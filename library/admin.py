from django.contrib import admin
from . models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'genre', 'shelf', 'borrower', 'date_borrowed', 'date_to_be_returned']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'occupation', 'student_number', 'financial_balance']

@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ['number', 'student', 'date_rented', 'date_expires', 'cost']