from django.shortcuts import render, redirect
from officer.models import HM_User
# from django.contrib.auth.decorators import login_required


def index(request):
    # hm_user = HM_User.objects.get(account=request.user)
    return render(request, 'hm_user/home/index.html')

