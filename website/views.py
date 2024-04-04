from django.shortcuts import render
from job.models import Job

def home(request):
    return render(request, 'website/home.html')


def job_listing(request):
    jobs = Job.objects.all()
    return render(request, 'website/job_listing.html', {'jobs': jobs})



def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    context = {'job': job}  # Corrected the key-value pair
    return render(request, 'website/job_details.html', context)
