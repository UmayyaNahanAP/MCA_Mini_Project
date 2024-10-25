from django.shortcuts import render, redirect
from officer.models import  Complaint
from vayal_user.models import Vayal_User
from vayal_user.forms import LeaseLand,LeaseLandForm




def index(request):
    lease_land=LeaseLand.objects.all()
    vayal_user = Vayal_User.objects.get(account=request.user)
    context = {
        'lease_land': lease_land,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/lease_land/index.html',context)



def create(request):
    print("1")
    vayal_user = Vayal_User.objects.get(account=request.user)
    print("2")
    if request.POST:
        print("3")
        form=LeaseLandForm(request.POST,request.FILES)
        print("4")
        print(form.errors)
        if form.is_valid():
            print("5")
            form.save()
            print("6")
            return redirect('vayal_user:lease_land')
    form=LeaseLandForm()
    context = {
        'form': form,
        'vayal_user': vayal_user,
    }
    print("7")
    return render(request,'vayal_user/lease_land/create.html',{'form': form,})