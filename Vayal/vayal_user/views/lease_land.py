from django.shortcuts import render, redirect
from officer.models import  Complaint
from vayal_user.models import Vayal_User
from vayal_user.forms import LeaseLand




def index(request):
    lease_land=LeaseLand.objects.all()
    return render(request,'vayal_user/lease_land/index.html',{'lease_land':lease_land})


# def create(request):
#     vayal_user = Vayal_User.objects.get(account=request.user)
#     if request.POST:
#         form = CreateComplaintForm(request.POST)
#         complaint = form.save(commit=False)
#         complaint.vayal_user = vayal_user
#         complaint.save()
#         return redirect('vayal_user:complaints')
#     form = CreateComplaintForm()
#     context = {
#         'vayal_user': vayal_user,
#         'form': form
#     }
#     return render(request, 'vayal_user/complaint/create.html', context)
