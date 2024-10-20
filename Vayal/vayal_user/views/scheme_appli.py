from django.shortcuts import render,redirect
from officer.models import SchemeApplication



def scheme_apply(request):
    if request.POST:
        form=SchemeApplication(request.POST)#,instance=schem)
        if form.is_valid():
            form.save()
            return redirect('/user/schemes/')
    form=SchemeApplication()
    return render(request,'user/schems/scheme_apply.html',{'form':form})