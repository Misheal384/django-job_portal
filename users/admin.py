from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_recruiter', 'is_applicant', 'is_approved')  # Include 'is_approved'
    search_fields = ('username', 'email')
    list_filter = ('is_recruiter', 'is_applicant', 'is_approved')  # Include 'is_approved'
    actions = ['approve_users']

    def approve_users(self, request, queryset):
        for user in queryset:
            user.is_approved = True
            user.save()
        self.message_user(request, "Selected users have been approved.")

    approve_users.short_description = "Approve selected users"
