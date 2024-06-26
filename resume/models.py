from django.db import models
from users.models import User

# Create your models here.
class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='Unknown')
    surname = models.CharField(max_length=100,default='Unknown')
    location = models.CharField(max_length=100, default='Unknown')
    job_title = models.CharField(max_length=100, default='Unknown')
    upload_resume = models.FileField(upload_to='resume')
    
    def __str__(self):
        return f'{self.first_name} {self.surname}'
