from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from officer.forms import Agricultural_officerRegistrationForm

def index(request):
    if request.POST: 
        form = Agricultural_officerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            officer = form.save(commit=False)
            account = User.objects.create_user(officer.name,form.cleaned_data['email'],form.cleaned_data['password'])
            account.save()
            officer.account = account
            officer.save()
            form.save()
            return redirect('login')
    form =Agricultural_officerRegistrationForm()
    return render(request,'vayal_user/reg/index.html',{'form':form})
