from django.contrib import admin
from .models import Scheme,SchemeApplication,VegetablePermission,Vegetable,Notification,Complaint


admin.site.register(Scheme)
admin.site.register(SchemeApplication)
admin.site.register(VegetablePermission)
admin.site.register(Vegetable)
admin.site.register(Notification)
admin.site.register(Complaint)
