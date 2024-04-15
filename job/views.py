from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Job
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
            form.save()
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