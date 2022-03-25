from django.shortcuts import render
# Create your views here.
class Job:
    def __init__(self, jobTitle, company, description, salary, contactInfo):
        self.jobTitle = jobTitle
        self.company = company
        self.description = description
        self.salary = salary
        self.contactInfo = contactInfo
        
jobs_data = [
    Job('Software Engineer', 'IBM', 'SQL and COBAL', 60000, '@ibm.com'),
    Job('Software Developer', 'Google', 'Mern Stack', 65000, '@google.com'),
    Job('Jr Backend Engineer', 'Kraken', 'Solidity and Rust', 60000, 'kraken.com/careers'),
    Job('Jr Frontend Engineer', 'Canva', 'HTML CSS Bootstrap', 50000, 'canva.com/careers'),
]
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jobs(request):
    print(jobs_data)
    return render(request, 'jobs/jobs.html', {'jobs_data': jobs_data})

