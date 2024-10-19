from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import urls
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from common.views import login_user

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html')),
    path('admin/', admin.site.urls),
    path('officer/',include('officer.urls')),
    path('user/',include('vayal_user.urls')),
    path('accounts/login/', login_user, name='login'),
    path('accounts/', include(urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)