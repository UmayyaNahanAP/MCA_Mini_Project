from django.shortcuts import render
from officer.models import Scheme
# from user.forms import SchemApplicationForm


# Create your views here.

def index(request):
    schemes=Scheme.objects.all()
    return render(request,'vayal_user/schemes/index.html',{'schemes':schemes})

def details(request,id):
    scheme=Scheme.objects.get(id=id)
    return render(request,'vayal_user/schemes/details.html',{'scheme':scheme})

# def schem_apply(request):
#     if request.POST:
#         form=SchemApplicationForm(request.POST)#,instance=schem)
#         if form.is_valid():
#             form.save()
#             return redirect('/user/schems/')
#     form=SchemApplicationForm()
#     return render(request,'user/schems/schem_apply.html',{'form':form})