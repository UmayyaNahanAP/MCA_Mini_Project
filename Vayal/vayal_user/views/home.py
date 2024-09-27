from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required


def index(request):
    # vayal_user = HM_User.objects.get(account=request.user)
    return render(request, 'vayal_user/home/index.html')

