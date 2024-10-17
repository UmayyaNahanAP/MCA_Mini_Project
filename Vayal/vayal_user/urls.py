from django.urls import path
from .views import reg, schemes,notification,home,complaint,vegetable

app_name='vayal_user'

urlpatterns = [

    path('home/',home.index,name='home'),
    path('register/',reg.index,name='register'),
    # path('login/',reg.login,name='login'),
    
    path('schemes/',schemes.index,name='scheme'),
    path('schemes/<int:id>/',schemes.details,name='details'),

    # path('apply-vegetable-permission/', views.vegetable_permission_view, name='vegetable_permission'),
    path('vegetables/', vegetable.vegetable_permission_view, name='vegetables'),
    path('vegetables/permission/', vegetable.vegetable_permission_view, name='vegetables'),

    path('complaints/', complaint.index, name='complaints'),
    path('complaints/create/', complaint.create, name='create_complaint'),

    path('notification/',notification.index, name='notifications'),
]