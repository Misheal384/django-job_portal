from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm  # corrected import statement


# Your view functions here...


#create a job
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method =='POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.is_available = True 
                var.save()
                messages.info(request, 'New job has been created')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form':form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')    
    


# Update a job
def update_job(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        messages.error(request, 'The job does not exist.')
        return redirect('dashboard')  # Or any other appropriate redirect

    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.is_available = job.is_available  # Preserve existing value
            job.save()
            messages.info(request, 'Job has been updated')
            return redirect('dashboard')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
        return render(request, 'job/update_job.html', context)

    # If the form is not valid, render the update job form again with validation errors
    context = {'form': form}
    return render(request, 'job/update_job.html', context)

            
    
#mange jobs retrieving list and passing htem to manage_jobs.html
def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs':jobs} 
    return render(request, 'job/manage_jobs.html',context)


#apply jobs
def apply_to_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Permission Denied')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
                job=job,
                user = request.user,
                status = 'Pending'
            )
            messages.info(request, 'You have succesfully applied! Please see dashboard')
            return redirect('dashboard')
    else:
        messages.info(request, 'Please log in to continue')
        return redirect('login')
    

def all_applicants(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context = {'job':job, 'applicants':applicants}
    return render(request, 'job/all_applicants.html', context)
    
    
    
    
    