from django import forms
from .models import Resume

class UpdateResumeForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    location = forms.CharField(required=True)
    job_title = forms.CharField(required=True)

    class Meta:
        model = Resume
        exclude = ('user',)
