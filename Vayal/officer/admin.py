from django.contrib import admin
from .models import Scheme,SchemeApplication,VegetablePermission,Notification,Complaint


admin.site.register(Scheme)
admin.site.register(SchemeApplication)
admin.site.register(VegetablePermission)
admin.site.register(Notification)
admin.site.register(Complaint)
