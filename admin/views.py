# admin/views.py
from django.shortcuts import render
from users.models import User
from job.models import Job, ApplyJob
from company.models import Company
from resume.models import Resume
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User


def admin_dashboard(request):
    user_count = User.objects.count()
    job_count = Job.objects.count()
    company_count = Company.objects.count()
    resume_count = Resume.objects.count()
    job_applications = ApplyJob.objects.filter(status='Pending').count()
    
    context = {
        'user_count': user_count,
        'job_count': job_count,
        'company_count': company_count,
        'resume_count': resume_count,
        'job_applications': job_applications,
    }
    return render(request, 'admin_dashboard.html', context)


def manage_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'admin/manage_users.html', context)

def toggle_user_status(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.info(request, f'User {user.username} status has been updated.')
    return redirect('manage_users')

# admin/views.py
from job.models import Job

def manage_jobs(request):
    if request.user.is_superuser:
        jobs = Job.objects.all()
        return render(request, 'admin/manage_jobs.html', {'jobs': jobs})
    else:
        return redirect('dashboard')
