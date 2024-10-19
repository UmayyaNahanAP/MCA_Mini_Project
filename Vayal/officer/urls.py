from django.urls import path
from .views import notification

app_name='officer'

urlpatterns = [
    path('notification/',notification.index, name='notification'),
    path('notification/<int:id>/',notification.details,name='details_notification'),
    path('notification/create/',notification.create, name='create_notification'),
    path('notification/<int:id>/update/',notification.update, name='update_notification'),
    path('notification/<int:id>/delete/',notification.delete, name='delete_notification'),



]