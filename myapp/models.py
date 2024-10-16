

# Create your models here.
from django.db import models 
from django.conf import settings


# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    message=models.TextField()

Doctor_CHOICES =(
    ('Orthopedics','Orthopedics'),
    ('Internal Medicine','Internal Medicine'),
    ('Obstetrics and Gynecology','Obstetrics and Gynecology'),
    ('Dermatology', 'Dermatology'),
    ('Pediatrics','Pediatric'),
    ('Radiology',' Radiology'),
    ('General Surgery',' General Surgery'),
    ('Ophthalmology','Ophthalmolog')




)

Gender_CHOICES=(
    ('Male','male'),
    ('Female','Female')
)

class Appointment(models.Model):
    Gender = models.CharField(choices=Gender_CHOICES, max_length=100)
    Age = models.IntegerField()
    Medical_Specialties = models.CharField(choices=Doctor_CHOICES, max_length=500)
    Date_and_time = models.DateTimeField()
    Patient_detail = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# from django.db import models
# from django.conf import settings

# class Hospital(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=200)

# class Ambulance(models.Model):
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
#     ambulance_number = models.CharField(max_length=50)
#     available = models.BooleanField(default=True)

# class Booking(models.Model):
#     ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     date_and_time = models.DateTimeField()
#     status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')])
