from django.shortcuts import render, redirect
from officer.models import Agricultural_officer,Complaint


def index(request):
    vayal_user = request.GET.get(' vayal_user')
    status = request.GET.get('status')
    complaints = Complaint.objects.all().order_by('-id')
    if  vayal_user:
        complaints = complaints.filter(vayal_user__name__icontains= vayal_user)
    if status:
        complaints = complaints.filter(status=status)
    context = {
        'vayal_user':  vayal_user,
        'status': status,
        'complaints': complaints,
    }
    return render(request, 'officer/complaint/index.html', context)

def details(request,id):
    vayal_user = request.GET.get(' vayal_user')
    complaint=Complaint.objects.get(id=id)
    context = {
        'vayal_user':  vayal_user,
        'complaint': complaint,
    }
    return render(request,'officer/complaint/details.html',context)


def mark_resolved(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.resolved = True
    complaint.save()
    return redirect('officer:complaints')


def update_status(request, id):
    officer =Agricultural_officer.objects.get(account=request.user)
    complaint = Complaint.objects.get(id=id)
    complaint.status = request.POST['status']
    complaint.officer =officer
    complaint.save()
    return redirect('officer:complaints')

def delete(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.delete()
    return redirect('officer:complaints')
