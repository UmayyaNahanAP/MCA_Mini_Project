from django.shortcuts import render, redirect
from officer.forms import CreateNotificationForm
from officer.models import Agricultural_officer,Notification


def index(request):
    status = request.GET.get('status')
    notifications = Notification.objects.all().order_by('-id')
    return render(request, 'officer/notification/index.html',{ 'notifications': notifications})

def details(request,id):
    notification=Notification.objects.get(id=id)
    return render(request,'officer/notification/details.html',{'notification':notification})


def create(request):
    officer =Agricultural_officer.objects.get(account=request.user)
    if request.POST:
        form = CreateNotificationForm(request.POST)
        if form.is_valid():
            create_notification= form.save(commit=False)
            create_notification.officer = officer
            create_notification .save()
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

