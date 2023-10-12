from django.contrib import admin
from . models import *

@admin.register(Treasury)
class TreasuryAdmin(admin.ModelAdmin):
    list_display = ['balance', 'cash', 'credit']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'cost', 'type']

@admin.register(Expence)
class ExpenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'cost', 'type']