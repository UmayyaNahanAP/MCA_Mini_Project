from django.contrib import admin
from django.urls import path,include
# from common.views import login_user
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/',login_user, name='login'),
    path('',include(urls)),
    path('officer/',include('officer.urls')),
    path('user/',include('hm_user.urls')),
]
