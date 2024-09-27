from django.shortcuts import render
from officer.models import Notification


def index(request):
    notifications = Notification.objects.filter(published=True)
    return render(request,'vayal_user/notification/index.html',{'notifications':notifications})