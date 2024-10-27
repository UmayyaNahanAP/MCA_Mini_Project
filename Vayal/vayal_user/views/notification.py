from django.shortcuts import render
from officer.models import Vayal_User,Notification


def index(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    notifications = Notification.objects.all().order_by('-id')
    return render(request,'vayal_user/notification/index.html',{'notifications': notifications,})

def details(request,id):
    vayal_user = Vayal_User.objects.get(account=request.user)
    notification=Notification.objects.get(id=id)
    context = {
        'notifications': notification,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/notification/details.html',context)