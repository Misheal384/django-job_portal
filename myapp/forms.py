from django import forms  
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,SetPasswordForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Contact
# from .models import Booking
  
User = get_user_model()  # Get the custom user model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')  
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email


class PasswordChangeForm(PasswordResetForm):
     email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )


class  Setpassword(SetPasswordForm):
     
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )





class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['Name','email','message']
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'})
        }



# class AmbulanceBookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['ambulance', 'date_and_time']
#         widgets = {
#             'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }