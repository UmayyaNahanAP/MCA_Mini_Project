from django.urls import path
from .views import schems,notification,home

app_name='vayal_user'

urlpatterns = [

    path('home/',home.index,name='home'),

    path('schems/',schems.index,name='index'),
    path('schems/<int:id>/',schems.details,name='details'),

    path('notification/',notification.index, name='notifications'),
]