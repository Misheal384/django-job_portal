from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')
        # Define required fields explicitly
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'location': forms.TextInput(attrs={'required': True}),
            'requirements': forms.Textarea(attrs={'required': True}),
            'ideal_candidate': forms.Textarea(attrs={'required': True}),
        }

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')
        # Define required fields explicitly
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'location': forms.TextInput(attrs={'required': True}),
            'requirements': forms.Textarea(attrs={'required': True}),
            'ideal_candidate': forms.Textarea(attrs={'required': True}),
        }
