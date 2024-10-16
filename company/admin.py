# company/admin.py
from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    search_fields = ('name', 'city', 'state')
