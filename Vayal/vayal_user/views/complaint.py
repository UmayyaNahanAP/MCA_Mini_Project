from django.shortcuts import render, redirect
from officer.models import  Vayal_User,Complaint
from officer.forms import CreateComplaintForm



def index(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    complaints = Complaint.objects.filter(vayal_user=vayal_user).order_by('-id')
    context = {
        'complaints': complaints,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/complaint/index.html', context)


def create(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    if request.POST:
        form = CreateComplaintForm(request.POST)
        complaint = form.save(commit=False)
        complaint.vayal_user = vayal_user
        complaint.save()
        return redirect('vayal_user:complaints')
    form = CreateComplaintForm()
    context = {
        'vayal_user': vayal_user,
        'form': form
    }
    return render(request, 'vayal_user/complaint/create.html', context)
