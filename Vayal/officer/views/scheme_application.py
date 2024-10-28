from django.shortcuts import render
from officer.models import  Agricultural_officer,Vayal_User,Scheme,SchemeApplication

def index(request,id):
    scheme=Scheme.objects.get(id=id)
    scheme_application= SchemeApplication.objects.filter(scheme=scheme)
    return render(request,'officer/scheme_application/index.html',{'scheme_application':scheme_application})

def user_details(request,application_id,vayal_user_id):
    scheme_application = SchemeApplication.objects.get(id=application_id, vayal_user_id=vayal_user_id)
    return render(request, 'officer/scheme_application/user_details.html', {'scheme_application': scheme_application})

def update_status(request,application_id,vayal_user_id):
    officer =Agricultural_officer.objects.get(account=request.user)
    scheme_application = SchemeApplication.objects.get(id=application_id, vayal_user_id=vayal_user_id)
    scheme_application.status = request.POST['status']
    scheme_application.officer =officer
    scheme_application.save()
    context = {
        'officer': officer,
        'scheme_application': scheme_application,
    }
    return render(request, 'officer/scheme_application/user_details.html', context)
