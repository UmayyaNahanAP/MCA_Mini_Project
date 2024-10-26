from django.shortcuts import render
from vayal_user.models import Vayal_User
from officer.models import Scheme,SchemeApplication

def index(request,id):
    scheme=Scheme.objects.get(id=id)
    scheme_application= SchemeApplication.objects.filter(scheme=scheme)
    return render(request,'officer/scheme_application/index.html',{'scheme_application':scheme_application})

def user_details(request,application_id,vayal_user_id):
    scheme_application = SchemeApplication.objects.get(id=application_id, vayal_user_id=vayal_user_id)
    return render(request, 'officer/scheme_application/user_details.html', {'scheme_application': scheme_application})

def update_status(request,application_id,vayal_user_id):
    scheme_application = SchemeApplication.objects.get(id=application_id, vayal_user_id=vayal_user_id)
    scheme_application.status = request.POST['status']
    scheme_application.save()
    return render(request, 'officer/scheme_application/user_details.html', {'scheme_application': scheme_application})


# def update_status(request, id):
#     scheme=Scheme.objects.get(id=id)
#     scheme_application =SchemeApplication.objects.filter(scheme=scheme)
#     scheme_application.status = request.POST['status']
#     scheme_application.save()
#     return render(request,'officer/scheme_application/index.html')

# def update_status(request, id):
#     complaint = Complaint.objects.get(id=id)
#     complaint.status = request.POST['status']
#     complaint.save()
#     return redirect('officer:complaints')

# def update_status(request, id):
#     vayal_user = Vayal_User.objects.get(account=request.user)
#     scheme=Scheme.objects.get(id=id)
#     scheme_appl =SchemeApplication.objects.filter(scheme=scheme)
#     scheme_application = scheme_appl.objects.filter(vayal_user=vayal_user)
#     scheme_application.status = request.POST['status']
#     scheme_application.save()
#     return render(request,'officer/scheme_application/index.html')



