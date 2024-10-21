from django.shortcuts import render
from officer.models import Notification


def index(request):
    notifications = Notification.objects.filter(published=True)
    return render(request,'vayal_user/notification/index.html',{'notifications':notifications})

def details(request,id):
    notification=Notification.objects.get(id=id)
    return render(request,'vayal_user/notification/details.html',{'notification':notification})