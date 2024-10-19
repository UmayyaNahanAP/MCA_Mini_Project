from django.urls import path,include


app_name='vayal_user'

urlpatterns = [
    path('user/',include('vayal_user.urls')),
]