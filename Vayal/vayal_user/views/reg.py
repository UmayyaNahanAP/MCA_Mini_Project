from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from officer.forms import VayalUserRegistrationForm



def index(request):
    if request.POST: 
        form = VayalUserRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            vayal_user = form.save(commit=False)
            account = User.objects.create_user(vayal_user.name,form.cleaned_data['email'],form.cleaned_data['password'])
            account.save()
            vayal_user.account = account
            vayal_user.save()
            # if not form.phone_number.isdigit() or len(form.phone_number) != 10:
            #     raise ValidationError("Phone number must be a 10-digit number.")
            form.save()
            return redirect('login')
    form = VayalUserRegistrationForm()
    return render(request,'vayal_user/reg/index.html',{'form':form})



# def index(request):
#     if request.POST: 
#         form = VayalUserRegistrationForm(request.POST,request.FILES)
#         if form.is_valid():
#             vayal_user = form.save(commit=False)
#             account = User.objects.create_user(vayal_user.name,form.cleaned_data['email'],form.cleaned_data['password'])
#             account.save()
#             vayal_user.account = account
#             vayal_user.save()
#             form.save()
#             return redirect('login')
#     form = VayalUserRegistrationForm()
#     return render(request,'vayal_user/reg/index.html',{'form':form})

