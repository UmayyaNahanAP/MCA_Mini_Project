from django.urls import path
from .views import schems,notification

app_name='officer'

urlpatterns = [
    path('schems/',schems.index,name='schems'),
    path('schems/create/',schems.create,name='create_schem'),
    path('schems/<int:id>/update/',schems.update,name='update_schem'),
    path('schems/<int:id>/',schems.details,name='details_schem'),
    path('schems/<int:id>/delete/',schems.delete,name='delete_schem'),

    path('notification/',notification.index, name='notifications'),
    path('notification/create/',notification.create, name='create_notification'),
    path('notification/<int:id>/update/',notification.update, name='update_notification'),
    path('notification/<int:id>/delete/',notification.delete, name='delete_notification'),
]