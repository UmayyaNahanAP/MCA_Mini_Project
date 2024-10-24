from django.shortcuts import render,redirect
from vayal_user.models import Vayal_User
from officer.forms import VegetablePermissionForm,Vegetable


def index(request):
    # vayal_user = Vayal_User.objects.get(account=request.user)
    vegetables=Vegetable.objects.all()
    context = {
        # 'vayal_user': vayal_user,
        'vegetables': vegetables}
    return render(request,'vayal_user/vegetable/index.html',context)
