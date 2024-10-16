# resume/admin.py
from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'location')
    search_fields = ('job_title', 'location')
