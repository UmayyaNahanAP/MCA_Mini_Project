from django.urls import path
from .views import notification,complaints

app_name='officer'

urlpatterns = [
    path('notification/',notification.index, name='notification'),
    path('notification/<int:id>/',notification.details,name='details_notification'),
    path('notification/create/',notification.create, name='create_notification'),
    path('notification/<int:id>/update/',notification.update, name='update_notification'),
    path('notification/<int:id>/delete/',notification.delete, name='delete_notification'),

    path('complaint/',complaints.index, name='complaints'),
    path('complaint/<int:id>/resolve/',complaints.mark_resolved, name='resolve_complaint'),
    path('complaint/<int:id>/update/',complaints.update_status, name='update_complaint_status'),
    path('complaint/<int:id>/delete/',complaints.delete, name='delete_complaint')



]