from django.contrib import admin
from .models import HM_User,Schem,Notification,Complaint

# Register your models here.

admin.site.register(HM_User)
admin.site.register(Schem)
admin.site.register(Notification)
admin.site.register(Complaint)
# admin.site.register(SchemApplication)