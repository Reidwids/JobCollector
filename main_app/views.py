from django.shortcuts import render
from .models import Job
# Create your views here.    

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jobs_index(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/jobs.html', {'jobs': jobs })

# def job_detail(request, job_id):
