from django.shortcuts import render,redirect
from vayal_user.models import Vayal_User
from officer.forms import VegetablePermissionForm,Vegetable


# def create(request):
#     student = Student.objects.get(account=request.user)
#     if request.POST:
#         form = CreateComplaintForm(request.POST)
#         complaint = form.save(commit=False)
#         complaint.student = student
#         complaint.save()
#         return redirect('student:complaints')
#     form = CreateComplaintForm()
#     context = {
#         'student': student,
#         'form': form
#     }
#     return render(request, 'student/complaint/create.html', context)

def vegetable_apply(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    if request.POST:
        form=VegetablePermissionForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.vayal_user = vayal_user
            application.save()
            return redirect('vayal_user:vegetables')
    form=VegetablePermissionForm()
    return render(request,'vayal_user/vegetable/application.html',{'form':form})


def index(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    vegetables=Vegetable.objects.all()
    context = {
        'vayal_user': vayal_user,
        'vegetables': vegetables}
    return render(request,'vayal_user/vegetable/index.html',context)


def add(request):
    vayal_user = Vayal_User.objects.get(account=request.user)
    if request.POST:
        form = Vegetable(request.POST)
        vegetable = form.save(commit=False)
        vegetable.vayal_user = vayal_user
        vegetable.save()
        return redirect('vayal_user:vegetables')
    form = Vegetable()
    context = {
        'vayal_user': vayal_user,
        'form': form
    }
    return render(request,'vayal_user/vegetable/add.html',context)