from django.shortcuts import render, redirect
from officer.models import VegetablePermission



def index(request):
    vayal_user = request.GET.get(' vayal_user')
    status = request.GET.get('status')
    vegetablepermission = VegetablePermission.objects.all()
    if  vayal_user:
        vegetablepermission = vegetablepermission.filter(vayal_user__name__icontains= vayal_user)
    if status:
        vegetablepermission = vegetablepermission.filter(status=status)
    context = {
        'vayal_user':  vayal_user,
        'status': status,
        'vegetablepermission': vegetablepermission,
    }
    return render(request,'officer/vegetable/index.html',context)


def mark_approved(request, id):
    vegetablepermission = VegetablePermission.objects.get(id=id)
    vegetablepermission.resolved = True
    vegetablepermission.save()
    return redirect('officer:vegetable_permission')


def update_status(request, id):
    vegetablepermission = VegetablePermission.objects.get(id=id)
    vegetablepermission.status = request.POST['status']
    vegetablepermission.save()
    return redirect('officer:vegetable_permission')


def delete(request, id):
    vegetablepermission =VegetablePermission.objects.get(id=id)
    vegetablepermission.delete()
    return redirect('officer:vegetable_permission')
