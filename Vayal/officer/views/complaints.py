from django.shortcuts import render, redirect
from officer.models import Complaint



def index(request):
    vayal_user = request.GET.get(' vayal_user')
    status = request.GET.get('status')
    complaints = Complaint.objects.all()
    if  vayal_user:
        complaints = complaints.filter(student__name__icontains= vayal_user)
    if status:
        complaints = complaints.filter(status=status)
    context = {
        'vayal_user':  vayal_user,
        'status': status,
        'complaints': complaints,
    }
    return render(request,'officer/complaint/index.html',context)


def mark_resolved(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.resolved = True
    complaint.save()
    return redirect('officer:complaints')


def update_status(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.status = request.POST['status']
    complaint.save()
    return redirect('officer:complaints')


def delete(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.delete()
    return redirect('officer:complaints')
