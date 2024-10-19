from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('officer/',include('officer.urls')),
    path('user/',include('vayal_user.urls')),
    path('accounts/', include(urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)