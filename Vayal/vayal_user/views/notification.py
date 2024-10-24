from django.shortcuts import render
from vayal_user.models import Vayal_User
from officer.models import Notification


def index(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    notifications = Notification.objects.filter(published=True)
    context = {
        'notifications': notifications,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/notification/index.html',context)

def details(request,id):
    vayal_user = Vayal_User.objects.get(account=request.user)
    notification=Notification.objects.get(id=id)
    context = {
        'notifications': notification,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/notification/details.html',context)