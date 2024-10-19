from django.urls import path
from .views import notification

app_name='vayal_user'

urlpatterns = [
    path('notification/',notification.index, name='notifications'),
    path('notification/create/',notification.create, name='create_notification'),
    path('notification/<int:id>/update/',notification.update, name='update_notification'),
    path('notification/<int:id>/delete/',notification.delete, name='delete_notification'),



]