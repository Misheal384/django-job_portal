from django.shortcuts import render, get_object_or_404
from .models import Condition
from django.shortcuts import render
from .models import FAQ, Resource, VideoTutorial, SupportGroup

def home(request):
    return render(request, 'education/home.html')

def condition_list(request):
    conditions = Condition.objects.all()
    return render(request, 'education/condition_list.html', {'conditions': conditions})

def condition_detail(request, pk):
    condition = get_object_or_404(Condition, pk=pk)
    return render(request, 'education/condition_detail.html', {'condition': condition})

def patient_resources(request):
    faqs = FAQ.objects.all()
    resources = Resource.objects.all()
    videos = VideoTutorial.objects.all()
    support_groups = SupportGroup.objects.all()

    return render(request, 'education/patient_resources.html', {
        'faqs': faqs,
        'resources': resources,
        'videos': videos,
        'support_groups': support_groups
    })

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Sending feedback via email (you can also save it to the database)
        send_mail(
            f'Feedback from {name}',
            message,
            email,
            ['info@example.com'],  # Replace with your email
            fail_silently=False,
        )
        
        messages.success(request, 'Thank you for your feedback!')
        return redirect('home')  # Redirect to home after submission
    
    return render(request, 'home.html')
