from django.shortcuts import render,redirect
from django.contrib.auth
from hm_user.forms import HMUserRegistrationForm

def index(request):
    if request.POST:
        form=HMUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form=HMUserRegistrationForm()
    return render(request,'hm_user/reg/index.html',{'form':form})