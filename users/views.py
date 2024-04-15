from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company

# register applicant only
def register_applicant(request):
    is_authenticated = request.user.is_authenticated

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created. Please login')
            return redirect('login')
        else:
            # Display form errors in messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'Error in {field}: {error}')
            # Render the form with errors
            return render(request, 'users/register_applicant.html', {'form': form, 'is_authenticated': is_authenticated})

    else:
        form = RegisterUserForm()
        context = {'form': form, 'is_authenticated': is_authenticated}
        return render(request, 'users/register_applicant.html', context)

#register recruiter only
def register_recruiter(request):
    is_authenticated = request.user.is_authenticated

    if request.method =='POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created.Please login')
            return redirect('login')
        else:
            # Display form errors in messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'Error in {field}: {error}')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form, 'is_authenticated': is_authenticated}
        return render(request, 'users/register_recruiter.html', context)

#login a user
def login_user(request):
    is_authenticated = request.user.is_authenticated

    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('login')
    else:
        return render(request, 'users/login.html', {'is_authenticated': is_authenticated})

#logout a  user
def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended.')
    return redirect('login')
