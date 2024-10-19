from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from vayal_user.forms import VayalUserRegistrationForm

def index(request):
    print("11")
    if request.POST: 
        print("22")
        form = VayalUserRegistrationForm(request.POST)
        print("33")
        print("44")
        print(form.errors)
        if form.is_valid():
            print("55")
            vayal_user = form.save(commit=False)
            account = User.objects.create_user(vayal_user.name,form.cleaned_data['email'],form.cleaned_data['password'])
            account.save()
            vayal_user.account = account
            vayal_user.save()
            form.save()
            return redirect('vayal_user:login')
    form = VayalUserRegistrationForm()
    return render(request,'vayal_user/reg/index.html',{'form':form})


def login(request):
     return render(request,'vayal_user/schems/index.html')


