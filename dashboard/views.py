from django.shortcuts import render, redirect
from job.models import ApplyJob

    
    
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# from django.shortcuts import render
# from job.models import ApplyJob

# def dashboard_view(request):
#     if request.user.is_authenticated:
#         user = request.user
#         jobs_applied_count = ApplyJob.objects.filter(user=user).count()
#     else:
#         jobs_applied_count = 0  # If not authenticated, set count to 0

#     context = {
#         'jobs_applied_count': jobs_applied_count,
#     }
#     return render(request, 'dashboard/dashboard.html', context)
