# admin.py
from django.contrib import admin
from .models import Contact, Appointment

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'email', 'message')  # Display relevant fields in the list view
    search_fields = ('Name', 'email')  # Allow searching by name and email
    ordering = ('-id',)  # Order by ID, or any other field you prefer

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('Patient_detail', 'Gender', 'Age', 'Medical_Specialties', 'Date_and_time')  # Display relevant fields
    list_filter = ('Medical_Specialties', 'Gender')  # Add filters based on specialties and gender
    search_fields = ('Patient_detail__username', 'Medical_Specialties')  # Allow searching by username and specialties
    ordering = ('-Date_and_time',)  # Order by date and time
