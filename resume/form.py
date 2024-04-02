from django import forms
from django.core.validators import RegexValidator
from .models import Resume


class UpdateResumeForm(forms.ModelForm):
    first_name = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z]+$', message='First name must only contain letters.')], required=True)
    surname = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z]+$', message='Surname must only contain letters.')], required=True)
    location = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z]+$', message='Job title must only contain letters.')], required=True)
    job_title = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z]+$', message='Job title must only contain letters.')], required=True)

    class Meta:
        model = Resume
        exclude = ('user',)
