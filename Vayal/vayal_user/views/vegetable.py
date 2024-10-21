from django.shortcuts import render,redirect
from officer.forms import VegetablePermissionForm,Vegetable





def vegetable_apply(request):
    if request.POST:
        form=VegetablePermissionForm(request.POST)#,instance=schem)
        if form.is_valid():
            form.save()
            return redirect('vayal_user/vegetable/index.html')
    form=VegetablePermissionForm()
    return render(request,'vayal_user/vegetable/application.html',{'form':form})


def index(request):
    vegetables=Vegetable.objects.all()
    return render(request,'vayal_user/vegetable/index.html',{'vegetables': vegetables})
