from django.shortcuts import render,redirect
from officer.models import Scheme
from vayal_user.models import Vayal_User
from officer.forms import SchemeApplicationForm
from django.db.models import Q


def index(request):
    vayal_user = Vayal_User.objects.get(account=request.user) 
    schemes = Scheme.objects.filter(Q(cast_eligibility__isnull=True) |  
                                    Q(cast_eligibility=vayal_user.cast) | 
                                    Q(cast_eligibility='All')).filter(
                                        Q(land_ownership=True) |
                                        Q(land_ownership=vayal_user.land_ownership) |
                                        Q(land_ownership='All')).order_by('-id')
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
    return render(request,'vayal_user/schemes/scheme_application.html',context)

