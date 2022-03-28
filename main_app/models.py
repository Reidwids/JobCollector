from django.db import models

# Create your models here.

class Job(models.Model):
        jobTitle = models.CharField(max_length=100)
        company = models.CharField(max_length=100)
        description = models.TextField(max_length=1000)
        salary = models.IntegerField()
        contactInfo = models.CharField(max_length=100)
