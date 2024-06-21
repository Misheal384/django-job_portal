from django.shortcuts import render
from job.models import Job, ApplyJob

def home(request):
    return render(request, 'website/home.html')


def job_listing(request):
    jobs = Job.objects.all().order_by('-timestamp')
    return render(request, 'website/job_listing.html', {'jobs': jobs})



def job_details(request, pk):
    if ApplyJob.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
        has_applied = False           
    job = Job.objects.get(pk=pk)
    context = {'job': job, 'has_applied':has_applied}
    return render(request, 'website/job_details.html', context)
