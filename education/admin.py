# admin.py
from django.contrib import admin
from .models import Condition, FAQ, Resource, VideoTutorial, SupportGroup

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the condition
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order by name

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)  # Display the question
    search_fields = ('question',)  # Allow searching by question
    ordering = ('question',)  # Order by question

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Display title and description
    search_fields = ('title',)  # Allow searching by title
    ordering = ('title',)  # Order by title

@admin.register(VideoTutorial)
class VideoTutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')  # Display title and URL
    search_fields = ('title',)  # Allow searching by title
    ordering = ('title',)  # Order by title

@admin.register(SupportGroup)
class SupportGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')  # Display name and website
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order by name
