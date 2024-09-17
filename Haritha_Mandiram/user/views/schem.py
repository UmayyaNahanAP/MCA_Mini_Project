from django.shortcuts import render,redirect
from officer.models import Schem,SchemApplication
from user.forms import SchemApplicationForm


# Create your views here.

def index(request):
    schems=Schem.objects.all()
    return render(request,'user/schem/index.html',{'schems':schems})

def details(request,id):
    schem=Schem.objects.get(id=id)
    return render(request,'user/schem/details.html',{'schem':schem})

def schem_apply(request,id):
    schem=Schem.objects.get(id=id)
    #form=SchemApplicationForm(instance=schem)
    if request.POST:
        form=SchemApplicationForm(request.POST)#,instance=schem)
        if form.is_valid():
            form.save()
            return redirect('/user/schem/')
    form=SchemApplicationForm()
    return render(request,'user/schem/schem_apply.html',{'form':form})