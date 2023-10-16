from django.contrib import admin
from . models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'author', 'genre', 'shelf', 'borrower', 'date_borrowed', 'date_to_be_returned']
    search_fields = ['borrower__first_name','borrower__last_name','borrower__student_number','genre','name','author']
    list_per_page = 10
    autocomplete_fields = ['borrower']
    list_filter = ['genre','date_borrowed','date_to_be_returned']

class BookInline(admin.TabularInline):
    readonly_fields = ['name','author', 'date_borrowed', 'date_to_be_returned','genre','shelf']
    model = Book
    extra = 0
@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ['number', 'student', 'date_rented', 'date_expires', 'cost']
    autocomplete_fields = ['student']
    search_fields = ['student__first_name', 'student__last_name', 'student__student_number']
    list_filter = ['cost','date_rented']
    list_per_page = 10

class LockerInline(admin.TabularInline):
    # readonly_fields = ['name','author', 'date_borrowed', 'date_to_be_returned','genre','shelf']
    model = Locker
    extra = 0
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'occupation', 'student_number', 'financial_balance','has_borrowed','locker']
    search_fields = ['first_name', 'last_name','student_number']
    list_filter = ['occupation']
    list_per_page = 10
    inlines = [BookInline,LockerInline]
    
    def has_borrowed(self,member):
        if len(member.books.all()) == 0:
            return 'no'
        else:
            return 'yes'
    def locker(self,member):
        return member.lockers
