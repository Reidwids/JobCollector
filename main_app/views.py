from django.shortcuts import render, redirect
from .models import Company, Job
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EventForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.    

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def jobs_index(request):
    jobs = Job.objects.filter(user = request.user)
    return render(request, 'jobs/jobs.html', {'jobs': jobs })

@login_required
def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    companies_missing = Company.objects.exclude(id__in = job.companies.all().values_list('id'))
    event_form = EventForm()
    return render(request, 'jobs/detail.html', {'job': job, 'event_form': event_form, 'companies': companies_missing})

@login_required
def add_event(request, job_id):
    form = EventForm(request.POST)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.job_id = job_id
        new_event.save()
    return redirect('detail', job_id = job_id)

@login_required
def assoc_company(request, job_id, company_id):
    Job.objects.get(id=job_id).companies.add(company_id)
    return redirect('detail', job_id=job_id)

@login_required
def unassoc_company(request, job_id, company_id):
    Job.objects.get(id=job_id).companies.remove(company_id)
    return redirect('detail', job_id=job_id)


class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['jobTitle', 'description','salary','contactInfo']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = '__all__'

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/companies/'

class CompanyList(LoginRequiredMixin, ListView):
    model = Company

class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company

class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'

class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'

class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = '/companies/'

