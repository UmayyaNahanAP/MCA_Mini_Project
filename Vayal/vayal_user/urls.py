from django.urls import path
from .views import schemes,reg,notification,complaint


app_name='vayal_user'

urlpatterns = [
    path('register/',reg.index,name='register'),

    path('schemes/',schemes.index,name='schemes'),
    path('schemes/<int:id>/',schemes.details,name='details_schemes'),


    path('notification/',notification.index, name='notifications'),
    path('notification/<int:id>/',notification.details,name='details_notification'),
    
    path('complaints/',complaint.index, name='complaints'),
    path('complaints/create/', complaint.create, name='create_complaint'),
]