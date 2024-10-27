from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from officer.models import Agricultural_officer, Vayal_User

User = get_user_model()


def login_user(request):
    if request.POST: 
        try:
            existing_user_name = User.objects.get(email=request.POST['username']).get_username()
            print(existing_user_name)
        except User.DoesNotExist:
            return render(request, 'registration/login.html', {"form": {'errors': ['invalid username']}})
        user = authenticate(request, username=existing_user_name, password=request.POST['password'])
        if user is not None:
            login(request, user)
            if Agricultural_officer.objects.filter(account=user).exists():
                return redirect('officer:home')
            elif Vayal_User.objects.filter(account=user).exists():
                return redirect('vayal_user:home')
        else:
            form = AuthenticationForm(request, request.POST)
            return render(request, 'registration/login.html', {"form": form})
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})
