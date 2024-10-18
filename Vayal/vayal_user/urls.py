from django.urls import path
from .views import reg

app_name='vayal_user'

urlpatterns = [

    path('register/',reg.index,name='register'),
    
    
]