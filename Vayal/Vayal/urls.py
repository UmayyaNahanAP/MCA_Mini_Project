from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('officer/',include('officer.urls')),
    path('user/',include('vayal_user.urls')),
    path('accounts/', include(urls)),
   
]