from django.urls import path,include


app_name='vayal_user'

urlpatterns = [
    path('officer/',include('officer.urls')),
]