from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.core.mail import send_mail 
from django.conf import settings
from .forms import  SignUpForm,ContactForm
from .models import Appointment 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.models import User
import logging
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# from .forms import AmbulanceBookingForm
# from .models import Booking

from django.core.exceptions import ValidationError 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView) 
from .forms import PasswordChangeForm,Setpassword 

from django.db.models import Q

logger = logging.getLogger(__name__)  # Get a logger instance

UserModel = get_user_model()


def signup(request):
    User = get_user_model()  # Get the custom user model
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        # Debugging: Log form validation process
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Set is_active to False for account activation
            user.save()
            logger.info("User %s created successfully but not activated yet.", user.username)
            
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            
            # Debugging: Log email recipient
            logger.info("Sending email to: %s", to_email)

            email = EmailMessage(mail_subject, message, to=[to_email])
            try:
                email.send()
                logger.info("Email sent successfully to %s.", to_email)
            except Exception as e:
                logger.error("Failed to send email: %s", e)
            
            return render(request, 'accounts/confirmation_message.html', {
                'message': 'Please confirm your email address to complete the registration.'
            })
        else:
            # Debugging: Log form errors
            logger.error("Form is not valid: %s", form.errors)
    
    # Return the form in case of GET request or invalid form
    return render(request, 'accounts/signup.html', {'form': form})




def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Render a template with a styled message and a button for login
        return render(request, 'accounts/activation_success.html', {'message': 'Thank you for your email confirmation. Now you can login to your account.'})
    else:
        # Render a template with an error message
        return render(request, 'accounts/activation_error.html', {'message': 'Activation link is invalid!'})



# Create your views here.

def Home(request):
    return render(request ,'index.html',{'act':'active'})

def health(request):
    return render(request,'health.html',{'active':'active'}) 

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        # messages.success(request,'Data has been submitted')
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})
#  
@login_required
def Appointmentfun(request):
    if request.method=='POST':
        # Patient_Name=request.POST['Patient_Name']
        try:
            Gender=request.POST['Gender']
            Age=request.POST['Age']
            Medical_Specialties=request.POST['Medical_Specialties']
            Date_and_time=request.POST['Date_and_time']
            user_obj=Appointment.objects.create(Gender=Gender,Age=Age,Medical_Specialties=Medical_Specialties,Date_and_time=Date_and_time)
            user_obj.Patient_detail=request.user
            user_obj.save()
            subject = 'Appointment Book'
            message = f'Hi {request.user.first_name}, your Appointment book in {Medical_Specialties} Department Your time slot booK { Date_and_time}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email ]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,"your appointment succesfully booked")
            
        except ValidationError:
            messages.warning(request,"value has an invalid format. It must be in YYYY-MM-DD HH:MM")
            
    return render(request,'appointment.html')

def loginfun(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('appointment')
        else:
            error_message = "Invalid username or password"
            messages.error(request, error_message)
            print(error_message)  # Print the error message to the terminal
    else:
        form = AuthenticationForm()
    
    return render(request, 'Auth/login_app.html', {'form': form})

def logoutfun(request):
    logout(request)
    return redirect('/') 

class PaswordresetviewFun(PasswordResetView):
    form_class=PasswordChangeForm
    template_name='Auth/password_reset.html'

class PasswordResetdoneviewFun(PasswordResetDoneView):
    template_name='Auth/password_reset_done.html'

class PasswordREsetConformViewFun(PasswordResetConfirmView):
    form_class=Setpassword
    template_name='Auth/password_reset_confirm.html'

class PasswordResetCompleteVIewFun(PasswordResetCompleteView):
    template_name='Auth/password_reset_complete.html' 

@login_required
def AppointmentDetail(request):
    user = request.user
    app = Appointment.objects.filter(Patient_detail=user).order_by('Date_and_time')  # Assuming ForeignKey relation to the user
    print(app)
    return render(request, 'Appointmentdetail.html', {'App': app})


# myapp/views.py


# def dashboardbook(request):
#     return render(request, 'dashboardbook.html')  # Adjust the template name as needed



# @login_required
# def create_booking(request):
#     if request.method == 'POST':
#         form = AmbulanceBookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             booking.save()
#             # Send confirmation email
#             return redirect('dashboardbook')
#     else:
#         form = AmbulanceBookingForm()

#     return render(request, 'ambulance_booking.html', {'form': form})