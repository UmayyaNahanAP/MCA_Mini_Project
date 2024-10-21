from django.shortcuts import render,redirect
from officer.forms import SchemeApplicationForm



def scheme_apply(request):
    if request.POST:
        form=SchemeApplicationForm(request.POST)#,instance=schem)
        if form.is_valid():
            form.save()
            return redirect('vayal_user/schemes/')
    form=SchemeApplicationForm()
    return render(request,'vayal_user/scheme_application/index.html',{'form':form})