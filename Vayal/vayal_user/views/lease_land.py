# from django.shortcuts import render, redirect
# from officer.models import  Complaint
# from vayal_user.models import Vayal_User
# from vayal_user.forms import LeaseLand,LeaseLandForm




# def index(request):
#     lease_land=LeaseLand.objects.all()
#     vayal_user = Vayal_User.objects.get(account=request.user)
#     context = {
#         'lease_land': lease_land,
#         'vayal_user': vayal_user,
#     }
#     return render(request,'vayal_user/lease_land/index.html',context)



# def create(request):
#     vayal_user = Vayal_User.objects.get(account=request.user)
#     if request.POST:
#         form=LeaseLandForm(request.POST,request.FILES)
#         lease_land = form.save(commit=False)
#         lease_land.vayal_user = vayal_user
#         lease_land.save()
#         if form.is_valid():
#             form.save()
#             return redirect('vayal_user:lease_land')
#     form=LeaseLandForm()
#     context = {
#         'form': form,
#         'vayal_user': vayal_user,
#     }
#     return render(request,'vayal_user/lease_land/create.html',context)