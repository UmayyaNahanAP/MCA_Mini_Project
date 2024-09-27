from django.shortcuts import render,redirect
from officer.models import Schem
from officer.forms import CreateSchemForm


def index(request):
    schems=Schem.objects.all()
    return render(request,'officer/schems/index.html',{'schems':schems})


def details(request,id):
    schem=Schem.objects.get(id=id)
    return render(request,'officer/schems/details.html',{'schem':schem})


def create(request):
    if request.POST:
        form=CreateSchemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('officer:schems')
    form=CreateSchemForm()
    return render(request,'officer/schems/create.html',{'form':form})


def update(request,id):
    schem=Schem.objects.get(id=id)
    form=CreateSchemForm(instance=schem)
    if request.POST:
        form=CreateSchemForm(request.POST,instance=schem)
        if form.is_valid():
            form.save()
            return redirect('officer:schems')
    return render(request,'officer/schems/update.html',{'form':form})


def delete(request,id):
    schem=Schem.objects.get(id=id)
    schem.delete()
    return redirect('officer:schems')