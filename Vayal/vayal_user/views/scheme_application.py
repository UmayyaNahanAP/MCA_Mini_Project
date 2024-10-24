from django.shortcuts import render,redirect
from vayal_user.models import Vayal_User
from officer.models import Scheme
from officer.forms import SchemeApplicationForm
from django.utils import timezone  
from django.http import HttpResponse

def scheme_apply(request,id):
    vayal_user = Vayal_User.objects.get(account=request.user)
    scheme= Scheme.objects.get(id=id)
    # if scheme.end_date < timezone.now().date():
    #     return HttpResponse("The application period for this scheme has ended.")
    if request.POST:
        form=SchemeApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            scheme_apply_form = form.save(commit=False)
            scheme_apply_form .vayal_user = vayal_user
            scheme_apply_form .scheme =  scheme
            scheme_apply_form .save()
            return redirect('vayal_user:schemes')
    form=SchemeApplicationForm(instance=scheme)
    return render(request,'vayal_user/scheme_application/index.html',{'form':form})