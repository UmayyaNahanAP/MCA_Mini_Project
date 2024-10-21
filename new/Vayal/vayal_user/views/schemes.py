from django.shortcuts import render
from officer.models import Scheme
# from user.forms import SchemApplicationForm


def index(request):
    schemes=Scheme.objects.all()
    return render(request,'vayal_user/schemes/index.html',{'schemes':schemes})

def details(request,id):
    scheme=Scheme.objects.get(id=id)
    return render(request,'vayal_user/schemes/details.html',{'scheme':scheme})

