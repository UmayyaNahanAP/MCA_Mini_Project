from django.shortcuts import render,redirect
from vayal_user.models import Vayal_User
from officer.models import Vegetable,VegetablePermission
from officer.forms import VegetablePermissionForm,VegetableForm


def index(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    vegetables=Vegetable.objects.all()
    context = {
        'vayal_user': vayal_user,
        'vegetables': vegetables}
    return render(request,'vayal_user/vegetable/index.html',context)

def add(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    if vayal_user.vegetable_permission_applied=="False" and vayal_user.vegetable_permission=="Pending":
        return redirect('vayal_user:vegetable_permission_application')
    if vayal_user.vegetable_permission_applied=="True" and vayal_user.vegetable_permission=="Pending":
        return redirect('vayal_user:vegetable_permission_status')
    if vayal_user.vegetable_permission_applied=="True" and vayal_user.vegetable_permission=="Approved":
        farm_details=VegetablePermission.objects.get(vayal_user=vayal_user)
        if request.POST:
            form = VegetableForm(request.POST,request.FILES)
            vegetable = form.save(commit=False)
            vegetable.farm_details = farm_details
            vegetable.save()
            return redirect('vayal_user:vegetables')
        form = VegetableForm()
        context = {
            'vayal_user': vayal_user,
            'form': form
        }
        return render(request,'vayal_user/vegetable/add.html',context)



def vegetable_apply(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    if request.POST:
        form=VegetablePermissionForm(request.POST,request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.vayal_user = vayal_user
            application.save()
            vayal_user.vegetable_permission_applied="True"
            vayal_user.vegetable_permission="Pending"
            vayal_user.save()
            return redirect('vayal_user:vegetable_permission_status')
    form=VegetablePermissionForm()
    return render(request,'vayal_user/vegetable/application.html',{'form':form})


def permission_status(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    try:
        vegetable_permission = VegetablePermission.objects.get(vayal_user=vayal_user)
    except VegetablePermission.DoesNotExist:
        vegetable_permission = None
    context = {
        'vayal_user': vayal_user,
        'vegetable_permission': vegetable_permission
    }
    return render(request,'vayal_user/vegetable/permission_status.html',context)


def add_vegetable(request,id):
    vayal_user = Vayal_User.objects.get(account=request.user)
    farm_details=VegetablePermissionForm.objects.get(id=id)
    if request.POST:
        form = VegetableForm(request.POST,request.FILES)
        vegetable = form.save(commit=False)
        vegetable.farm_details = farm_details
        vegetable.save()
        return redirect('vayal_user:vegetables')
    form = VegetableForm()
    context = {
        'farm_details': vayal_user,
        'form': form
    }
    return render(request,'vayal_user/vegetable/add.html',context)


# def buy(request,id):
#     vayal_user = Vayal_User.objects.get(account=request.user)
#     if request.POST:
#         form = VegetableForm(request.POST,request.FILES)
#         vegetable = form.save(commit=False)
#         vegetable.farm_details = farm_details
#         vegetable.save()
#         return redirect('vayal_user:vegetables')
#     form = VegetableForm()
#     context = {
#         'farm_details': vayal_user,
#         'form': form
#     }
#     return render(request,'vayal_user/vegetable/add.html',context)