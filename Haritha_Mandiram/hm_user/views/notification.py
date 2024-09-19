from django.shortcuts import render
from officer.models import Notification


def index(request):
    status = request.GET.get('status')
    notifications = Notification.objects.all()
    if status:
        notifications = notifications.filter(published=status == 'published')
    context = {
        'notifications': notifications,
        'status': status
    }
    return render(request, 'hm_user/notification/index.html', context)