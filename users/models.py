from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator, MaxLengthValidator

class User(AbstractUser):
    # Unique email field with email validation
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Please enter a valid email address.")])
    
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)

    # Mobile number validation (only allows digits and a specific length)
    mobile_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$', 
                message="Mobile number must be entered in the format: '+2333'. Up to 15 digits allowed."
            )
        ]
    )
    
    # Ghana card number validation (adjust regex as necessary for your requirements)
    ghana_card_number = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10,20}$',  # Example: allows only digits and 10-20 characters
                message="Ghana card number must be numeric and between 10 to 20 digits."
            )
        ]
    )

    first_name = models.CharField(max_length=150, default='DefaultFirstName')
    last_name = models.CharField(max_length=150, default='DefaultLastName')
    
    is_approved = models.BooleanField(default=False)  # New field to track approval

    # Override save method to enforce any additional validation if necessary
    def save(self, *args, **kwargs):
        # Example: Ensure only one of is_recruiter or is_applicant can be True
        if self.is_recruiter and self.is_applicant:
            raise ValueError("A user cannot be both a recruiter and an applicant.")
        super().save(*args, **kwargs)
