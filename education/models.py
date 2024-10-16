from django.db import models

class Condition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    symptoms = models.TextField()
    causes = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    home_management = models.TextField()
    warning_signs = models.TextField()

    def __str__(self):
        return self.name



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')

    def __str__(self):
        return self.title

class VideoTutorial(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class SupportGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name