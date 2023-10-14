from django.contrib import admin
from . models import *

@admin.register(Treasury)
class TreasuryAdmin(admin.ModelAdmin):
    list_display = ['balance', 'cash', 'credit']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'cost', 'type']
    search_fields = ['title', 'cost']
    list_filter = ['type','date']

@admin.register(Expence)
class ExpenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'cost', 'type']
    search_fields = ['title', 'cost']
    list_filter = ['type','date']