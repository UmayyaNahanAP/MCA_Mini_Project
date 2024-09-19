from django.urls import path
from .views import reg,schems,notification,home

app_name='hm_user'

urlpatterns = [
    path('home/',home.index,name='home'),
    path('sign_up/',reg.index,name='sign_up'),
    path('login/',login,name='home'),

    path('schems/',schems.index,name='index'),
    path('schems/<int:id>/',schems.details,name='details'),

    path('notification/',notification.index, name='notifications'),
    
]