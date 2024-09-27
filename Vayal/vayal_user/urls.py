from django.urls import path
from .views import schems,notification

app_name='vayal_user'

urlpatterns = [

    path('schems/',schems.index,name='index'),
    path('schems/<int:id>/',schems.details,name='details'),

    path('notification/',notification.index, name='notifications'),
]