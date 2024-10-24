from django.shortcuts import render, redirect
from vayal_user.models import Vayal_User


def index(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    return render(request, 'vayal_user/home/index.html',{'vayal_user': vayal_user})

