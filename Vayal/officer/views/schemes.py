from django.shortcuts import render,redirect
from officer.models import Agricultural_officer,Scheme
from officer.forms import CreateSchemeForm


def index(request):
    officer =Agricultural_officer.objects.get(account=request.user)
    schemes=Scheme.objects.all().order_by('-id')
    context = {
        'officer': officer,
        'schemes':schemes,
    }
    return render(request,'officer/schemes/index.html',context)


def details(request,id):
    scheme=Scheme.objects.get(id=id)
    return render(request,'officer/schemes/details.html',{'scheme':scheme})


def create(request):
    if request.POST:
        form=CreateSchemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('officer:schemes')
    form=CreateSchemeForm()
    return render(request,'officer/schemes/create.html',{'form':form})


def update(request,id):
    scheme=Scheme.objects.get(id=id)
    form=CreateSchemeForm(instance=scheme)
    if request.POST:
        form=CreateSchemeForm(request.POST,instance=scheme)
        if form.is_valid():
            form.save()
            return redirect('officer:schemes')
    return render(request,'officer/schemes/update.html',{'form':form})


def delete(request,id):
    scheme=Scheme.objects.get(id=id)
    scheme.delete()
    return redirect('officer:schemes')