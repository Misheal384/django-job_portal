from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume
from .form import UpdateResumeForm
from users.models import User

def update_resume(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateResumeForm(request.POST, instance=resume)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(pk=request.user.id)
                user.has_resume = True
                user.save()
                var.save()
                messages.info(request, 'Your resume info has been updated.')
                return redirect('dashboard')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.warning(request, f'Error in {field}: {error}')
                
                # Display non-field errors
                for error in form.non_field_errors():
                    messages.warning(request, error)
        else:
            form = UpdateResumeForm(instance=resume)
        context = {'form': form}
        return render(request, 'resume/update_resume.html', context)
    else:
        messages.warning(request, 'Permission denied')
        return render(request, 'dashboard', {'message': 'Permission denied'})
def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume': resume}
    return render(request, 'resume/_details.html', context)