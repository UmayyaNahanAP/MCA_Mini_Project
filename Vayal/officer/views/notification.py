from django.shortcuts import render, redirect
from officer.forms import CreateNotificationForm
from officer.models import Notification


def index(request):
    status = request.GET.get('status')
    notifications = Notification.objects.all().order_by('-id')
    if status:
        notifications = notifications.filter(published=status == 'published')
    context = {
        'notifications': notifications,
        'status': status
    }
    return render(request, 'officer/notification/index.html', context)

def details(request,id):
    notification=Notification.objects.get(id=id)
    return render(request,'officer/notification/details.html',{'notification':notification})


def create(request):
    if request.POST:
        form = CreateNotificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('officer:notifications')
    form = CreateNotificationForm()
    return render(request, 'officer/notification/create.html/', {'form': form})


def update(request, id):
    notification = Notification.objects.get(id=id)
    if request.POST:
        form = CreateNotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('officer:notifications')
    form = CreateNotificationForm(instance=notification)
    return render(request, 'officer/notification/update.html', {'form': form})


def delete(request, id):
    notification = Notification.objects.get(id=id)
    notification.delete()
    return redirect('officer:notifications')

