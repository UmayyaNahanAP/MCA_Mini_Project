from django.shortcuts import render,redirect
from vayal_user.models import Vayal_User
from officer.models import VegetablePermission
from officer.forms import VegetablePermissionForm,Vegetable


def index(request):
    status = request.GET.get('status')
    vegetable_permissions= VegetablePermission.objects.all().order_by('-id')
    if status:
        vegetable_permissions = vegetable_permissions.filter(status=status)
    context = {
        'status': status,
        'vegetable_permissions': vegetable_permissions,
    }
    return render(request,'officer/vegetable/index.html',context)


def user_details(request,application_id,vayal_user_id):
    vegetable_permission = VegetablePermission.objects.get(id=application_id, vayal_user_id=vayal_user_id)
    return render(request, 'officer/vegetable/user_details.html', {'vegetable_permission': vegetable_permission})

def update_status(request,application_id,vayal_user_id):
    vegetable_permission = VegetablePermission.objects.get(id=application_id, vayal_user_id=vayal_user_id)
    vayal_user = vegetable_permission.vayal_user
    vayal_user.vegetable_permission = request.POST['status']
    vayal_user.save()
    status = request.GET.get('status')
    vegetable_permissions= VegetablePermission.objects.all().order_by('-id')
    if status:
        vegetable_permissions = vegetable_permissions.filter(status=status)
    context = {
        'status': status,
        'vegetable_permissions': vegetable_permissions,
    }
    return render(request,'officer/vegetable/index.html',context)
