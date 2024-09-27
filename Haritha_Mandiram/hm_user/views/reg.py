from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from hm_user.forms import HMUserRegistrationForm
from officer.models import HM_User

def index(request):
    if request.POST: 
        print("ddsxvc")
        form = HMUserRegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            hm_user = form.save(commit=False)
            account = User.objects.create_user(hm_user.name,form.cleaned_data['email'],form.cleaned_data['password'])
            account.save()
            hm_user.account = account
            hm_user.save()
            form.save()
            return redirect('hm_user:login')
        else:
            print(form.errors)
    print("dds")
    form = HMUserRegistrationForm()
    return render(request,'hm_user/reg/index.html',{'form':form})



# def index(request):
#     print(request)
#     if request.method == "POST":
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = HMUserRegistrationForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user =user_form.save(commit=False)
#             profile = profile_form.save()
#             profile.user = user
#             profile.save()
#             user.save()
#             # messages.success(request,('Your profile was successfully updated!'))
#             return redirect('hm_user:login')
#     user_form = UserForm(instance=request.user)
#     profile_form = HMUserRegistrationForm(instance=request.user.profile)
#     return render(request,'hm_user/reg/index.html',{'form':user_form})


# def index(request):
#     if request.POST:
#         form = HMUserRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             hm_user = form.save(commit=False)
#             account = User.objects.create_user(
#                 hm_user.name, form.cleaned_data['email'], form.cleaned_data['password'])
#             account.save()
#             hm_user.account = account
#             hm_user.save()
#             form.save()
#             return redirect('hm_user:login')
#     form = HMUserRegistrationForm()
#     return render(request,'hm_user/reg/index.html',{'form':form})



# def index(request):
#     if request.POST:
#         form = HMUserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             hm_user = HM_User.objects.create(account=user, **form.cleaned_data)
#             # hm_user = form.save(commit=False)
#             # account = User.objects.create_user(
#             #     hm_user.name, form.cleaned_data['email'], form.cleaned_data['password'])
#             # account.save()
#             # hm_user.account = account
#             hm_user.save()
#             # form.save()
#             return redirect('hm_user:login')
#     form = HMUserRegistrationForm()
#     return render(request,'hm_user/reg/index.html',{'form':form})

# def index(request):
#     if request.POST:
#         form = HMUserRegistrationForm(request.POST)
#         if form.is_valid():
#             hm= form.save(commit=False)
#             username=hm.name
#             email=form.email
#             password=form.password
#             account = User.objects.create_user(username,email,password)
#             account.save()
#             hm.account = account
#             hm.save()
#             # form.save()
#             return redirect('hm_user:login')
#     form = HMUserRegistrationForm()
#     return render(request,'hm_user/reg/index.html',{'form':form})

def login(request):
     return render(request,'hm_user/schems/index.html')


# def index(request):
#     if request.POST:
#         form = HMUserRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             hm_user = form.save(commit=False)
#             account = User.objects.create_user(
#                 hm_user.name, form.cleaned_data['email'], form.cleaned_data['password'])
#             account.save()
#             hm_user.account = account
#             hm_user.save()
#             form.save()
#             return redirect('hm_user:login')
#     form = HMUserRegistrationForm()
#     return render(request,'hm_user/reg/index.html',{'form':form})