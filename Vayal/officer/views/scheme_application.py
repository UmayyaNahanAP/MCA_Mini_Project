from django.shortcuts import render
from officer.models import Scheme,SchemeApplication

def index(request,id):
    #vayal_user = Vayal_User.objects.get(account=request.user)
    scheme=Scheme.objects.get(id=id)
    scheme_application= SchemeApplication.objects.filter(scheme=scheme)
    # for application in scheme_application:
    #     vayal_user = application.vayal_user 
    # context = {
    #     'scheme': scheme,
    #     ' scheme_application':  scheme_application
    # }
    return render(request,'officer/scheme_application/index.html',{'scheme_application':scheme_application})