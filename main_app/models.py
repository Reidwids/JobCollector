from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

EVENTS = (
        ('I', 'Interviews'),
        ('D', 'Deadlines'),
)
class Company(models.Model):
        name = models.CharField(max_length=50)
        description = models.CharField(max_length=50)
        def __str__(self):
                return self.name
        def get_absolute_url(self):
            return reverse("companies_detail", kwargs={"pk": self.id})
        
class Job(models.Model):
        jobTitle = models.CharField(max_length=100)
        description = models.TextField(max_length=1000)
        salary = models.IntegerField()
        contactInfo = models.CharField(max_length=100)
        companies = models.ManyToManyField(Company)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        def get_absolute_url(self):
            return reverse('detail', kwargs = {'job_id': self.id})
        def __str__(self):
                return self.jobTitle

class Event(models.Model):
        type = models.CharField(max_length=1, choices=EVENTS, default=EVENTS[0][0])
        job = models.ForeignKey(Job, on_delete=models.CASCADE)
        date = models.DateField('Event Date')
        description = models.CharField(max_length=100)
        def __str__(self):
                return f'{self.get_type_display()} on {self.date}'
