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

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'phone_number', 'user']

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['librarian','day', 'start_time', 'end_time']