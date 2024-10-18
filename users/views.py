from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company

# Register applicant only
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
            messages.info(request, 'Your account has been created. Please login.')
            return redirect('login')
        else:
            # Display form errors in messages and print them to the terminal
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'Error in {field}: {error}')
                    print(f'Error in {field}: {error}')  # Print error to the terminal
            # Render the form with errors
            return render(request, 'users/register_applicant.html', {'form': form, 'is_authenticated': is_authenticated})

    else:
        form = RegisterUserForm()
        context = {'form': form, 'is_authenticated': is_authenticated}
        return render(request, 'users/register_applicant.html', context)


# Register recruiter only
def register_recruiter(request):
    is_authenticated = request.user.is_authenticated

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created. Please login.')
            return redirect('login')
        else:
            # Display form errors in messages and render the form with errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'Error in {field}: {error}')
                    print(f'Error in {field}: {error}')  # Print error to the terminal
            # Render the form with errors instead of redirecting
            return render(request, 'users/register_recruiter.html', {'form': form, 'is_authenticated': is_authenticated})
    
    else:
        form = RegisterUserForm()
        context = {'form': form, 'is_authenticated': is_authenticated}
        return render(request, 'users/register_recruiter.html', context)

#login a user
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def login_user(request):
    is_authenticated = request.user.is_authenticated

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active and user.is_approved:  # Check if the user is approved
                login(request, user)
                print(f"Logged in user: {user}")
                return redirect('dashboard')
            else:
                # Approval message and print statement added here
                messages.warning(request, 'Your account is not approved yet.')
                print(f"Approval message triggered for user: {email}")  # Log the approval message
                return redirect('login')
        else:
            messages.warning(request, 'Invalid email or password.')
            return redirect('login')
    else:
        return render(request, 'users/login.html', {'is_authenticated': is_authenticated})

    


#logout a  user
def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended.')
    return redirect('login')




