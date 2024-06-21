from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    
    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)

    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    ghana_card_number = models.CharField(max_length=20, blank=True, null=True)

    first_name = models.CharField(max_length=150, default='DefaultFirstName')
    last_name = models.CharField(max_length=150, default='DefaultLastName')
