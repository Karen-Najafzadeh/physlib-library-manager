from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name']

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'user', 'phone_number' ]
    search_fields = ['user__first_name', 'user__last_name','student_number']

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['librarian','day', 'start_time', 'end_time']
    search_fields = ['librarian__user__first_name']
    list_filter = ['day','librarian']
    ordering = ['day', 'start_time']