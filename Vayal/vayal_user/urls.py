from django.urls import path
from .views import reg,home,schemes,scheme_application,notification,complaint,vegetable,lease_land


app_name='vayal_user'

urlpatterns = [
    path('register/',reg.index,name='register'),
    # path('login/',reg.login,name='login'),
    path('home/',home.index,name='home'),

    path('schemes/',schemes.index,name='schemes'),
    path('schemes/<int:id>/',schemes.details,name='details_schemes'),
    
    path('schemes/<int:id>/scheme_apply/',scheme_application.scheme_apply,name='scheme_apply'),
    # path('scheme_apply/<int:id>',scheme_application.scheme_apply,name='scheme_apply/'),
    
    path('vegetables/',vegetable.index,name='vegetables'),
    path('vegetable/permission_application/',vegetable.vegetable_apply,name='vegetable_permission_application'),
    path('vegetables/add/',vegetable.add,name='vegetables_add'),

    path('lease_land/',lease_land.index,name='lease_land'),

    path('notification/',notification.index, name='notifications'),
    path('notification/<int:id>/',notification.details,name='details_notification'),
    
    path('complaints/',complaint.index, name='complaints'),
    path('complaints/create/', complaint.create, name='create_complaint'),
]