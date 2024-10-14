from django.urls import path
from .views import reg, schemes,notification,home,complaint

app_name='vayal_user'

urlpatterns = [

    path('home/',home.index,name='home'),
    path('register/',reg.index,name='register'),
    # path('login/',reg.login,name='login'),
    
    path('schemes/',schemes.index,name='scheme'),
    path('schemes/<int:id>/',schemes.details,name='details'),

    path('complaints/', complaint.index, name='complaints'),
    path('complaints/create/', complaint.create, name='create_complaint'),

    path('notification/',notification.index, name='notifications'),
]