from django.urls import path
from .views import reg,home,schemes,scheme_application,notification,complaint,vegetable,lease_land


app_name='vayal_user'

urlpatterns = [
    path('register/',reg.index,name='register'),
    # path('login/',reg.login,name='login'),
    path('home/',home.index,name='home'),

    path('schemes/',schemes.index,name='schemes'),
    path('schemes/<int:id>/',schemes.details,name='details_schemes'),
    path('schemes/<int:id>/scheme_apply/',schemes.scheme_apply,name='scheme_apply'),
    path('schemes/applied_schemes',schemes.applied_schemes,name='applied_schemes'),
    
    path('vegetables/',vegetable.index,name='vegetables'),
    path('vegetables/add_button/',vegetable.add,name='add_button'),
    path('vegetable/permission_application/',vegetable.vegetable_apply,name='vegetable_permission_application'),
    path('vegetable/permission_status/',vegetable.permission_status,name='vegetable_permission_status'),
    path('vegetables/<int:id>/add_vegetable/',vegetable.add_vegetable,name='vegetables_add'),
    path('vegetables/<int:id>/buy/',vegetable.buy_vegetable,name='vegetables_purchase'),

    path('lease_land/',lease_land.index,name='lease_land'),
    path('lease_land/create',lease_land.create,name='create_lease_land'),

    path('notification/',notification.index, name='notifications'),
    path('notification/<int:id>/',notification.details,name='details_notification'),
    
    path('complaints/',complaint.index, name='complaints'),
    path('complaints/create/', complaint.create, name='create_complaint'),
]