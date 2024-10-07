from django.contrib import admin
from .models import Appointment, Contact

# Register your models here.
admin.site.register(Contact)

# @admin.register(Appointment)
# class AppointMentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'Medical_Specialties', 'Date_and_time', 'Patient_name']  # Use the correct field name
#     search_fields = ['Patient_name', 'id']
