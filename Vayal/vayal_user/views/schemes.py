from django.shortcuts import render
from officer.models import Scheme
from vayal_user.models import Vayal_User


def index(request):
    schemes=Scheme.objects.all()
    vayal_user = Vayal_User.objects.get(account=request.user)
    context = {
        'schemes': schemes,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/schemes/index.html',context)

def details(request,id):
    scheme=Scheme.objects.get(id=id)
    vayal_user = Vayal_User.objects.get(account=request.user)
    context = {
        'scheme': scheme,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/schemes/details.html',context)

