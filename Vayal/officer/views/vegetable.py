from django.shortcuts import render,redirect
from vayal_user.models import Vayal_User
from officer.models import VegetablePermission
from officer.forms import VegetablePermissionForm,Vegetable


def index(request):
    vegetable_permissions= VegetablePermission.objects.all().order_by('-id')
    return render(request,'officer/vegetable/index.html', {'vegetable_permissions':  vegetable_permissions})



def user_details(request,application_id,vayal_user_id):
    vegetable_permission = VegetablePermission.objects.get(id=application_id,vayal_user_id=vayal_user_id)
    return render(request, 'officer/vegetable/user_details.html', {'vegetable_permission': vegetable_permission})


# def user_details(request,application_id,vayal_user_id):
#     scheme_application = SchemeApplication.objects.get(id=application_id, vayal_user_id=vayal_user_id)
#     return render(request, 'officer/scheme_application/user_details.html', {'scheme_application': scheme_application})
