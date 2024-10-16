# job/admin.py
from django.contrib import admin
from .models import Job, ApplyJob, State, Industry

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'city', 'is_available', 'job_type')
    search_fields = ('title', 'company__name', 'city')
    list_filter = ('is_available', 'job_type')

@admin.register(ApplyJob)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status')
    search_fields = ('job__title', 'user__username')
    list_filter = ('status',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name',)
