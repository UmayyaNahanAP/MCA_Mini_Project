from django.shortcuts import render,redirect
from officer.models import Schem
# from user.forms import SchemApplicationForm


# Create your views here.

def index(request):
    schems=Schem.objects.all()
    return render(request,'hm_user/schems/index.html',{'schems':schems})

def details(request,id):
    schem=Schem.objects.get(id=id)
    return render(request,'hm_user/schems/details.html',{'schem':schem})

# def schem_apply(request):
#     if request.POST:
#         form=SchemApplicationForm(request.POST)#,instance=schem)
#         if form.is_valid():
#             form.save()
#             return redirect('/user/schems/')
#     form=SchemApplicationForm()
#     return render(request,'user/schems/schem_apply.html',{'form':form})