from django.shortcuts import render,redirect
from vayal_user.models import Vayal_User
from officer.models import Scheme
from officer.forms import SchemeApplicationForm

def scheme_apply(request,id):
    vayal_user = Vayal_User.objects.get(account=request.user)
    scheme= Scheme.objects.get(id=id)
    if request.POST:
        form=SchemeApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            scheme_apply_form = form.save(commit=False)
            scheme_apply_form .vayal_user = vayal_user
            scheme_apply_form .scheme =  scheme
            scheme_apply_form .save()
            return redirect('vayal_user:schemes')
    form=SchemeApplicationForm(instance=scheme)
    context = {
        'form': form,
        'scheme':scheme,
        'vayal_user': vayal_user,
    }
    return render(request,'vayal_user/scheme_application/index.html',context)