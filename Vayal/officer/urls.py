from django.urls import path,include
from .views import home,schemes,notification,complaints,vegetable,scheme_application

app_name='officer'

urlpatterns = [
   
    path('home/',home.index,name='home'),
    path('home/users',home.users,name='home_users'),

    path('schemes/',schemes.index,name='schemes'),
    path('schemes/create/',schemes.create,name='create_schemes'),
    path('schemes/<int:id>/update/',schemes.update,name='update_schemes'),
    path('schemes/<int:id>/',schemes.details,name='details_schemes'),
    path('schemes/<int:id>/delete/',schemes.delete,name='delete_schemes'),
    
    path('schemes/<int:id>/applied_users',scheme_application.index,name='applied_users'),
    path('user_details/<int:application_id>/<int:vayal_user_id>/',scheme_application.user_details, name='applied_user_details'),
    path('schemes/applied_users/<int:application_id>/<int:vayal_user_id>/update/',scheme_application.update_status, name='update_applied_users_status'),

    path('vegetables/',vegetable.index,name='vegetables'),
    path('vegetables/user_details/<int:application_id>/<int:vayal_user_id>/',vegetable.user_details, name='vegetable_applied_user_details'),
    path('vegetables/applied_users/<int:application_id>/<int:vayal_user_id>/update/',vegetable.update_status, name='update_vegetable_applied_users_status'),

    path('notification/',notification.index, name='notifications'),
    path('notification/<int:id>/',notification.details,name='details_notification'),
    path('notification/create/',notification.create, name='create_notification'),
    path('notification/<int:id>/update/',notification.update, name='update_notification'),
    path('notification/<int:id>/delete/',notification.delete, name='delete_notification'),

    path('complaint/',complaints.index, name='complaints'),
    path('complaint/details/<int:id>',complaints.details, name='complaints_details'),
    path('complaint/<int:id>/resolve/',complaints.mark_resolved, name='resolve_complaint'),
    path('complaint/<int:id>/update/',complaints.update_status, name='update_complaint_status'),
    path('complaint/<int:id>/delete/',complaints.delete, name='delete_complaint')



]