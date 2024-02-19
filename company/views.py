from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from .form import UpdateCompanyForm
from users.models import User

# updating company because the company is already created
def update_company(request):
    company = Company.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            var = form.save(commit=False)
            user = User.objects.get(id=request.user.id)  # Use request.user.id
            user.has_company = True
            var.save()
            user.save()
            messages.info(request, 'Your company info has been updated. You can start creating job ads')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateCompanyForm(instance=company)
        context = {'form':form}  
        return render(request, 'company/update_company.html', context)  


#view company details
def company_details(request, pk): #pk is primarykey
    company = Company.objects.get(pk=pk)
    context = {'company':company}
    return render(request, 'company/company_details.html', context)