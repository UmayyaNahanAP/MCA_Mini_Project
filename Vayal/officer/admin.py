from django.contrib import admin
from .models import Vayal_User,Agricultural_officer,Scheme,SchemeApplication,VegetablePermission,Vegetable,VegetablePurchase,Complaint,Notification,LeaseLand

admin.site.register(Vayal_User)
admin.site.register(Agricultural_officer)
admin.site.register(Scheme)
admin.site.register(SchemeApplication)
admin.site.register(VegetablePermission)
admin.site.register(Vegetable)
admin.site.register(VegetablePurchase)
admin.site.register(Complaint)
admin.site.register(Notification)
admin.site.register(LeaseLand)