"""
URL configuration for dotshirt project.
"""

from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),


    path('admin/', admin.site.urls),

    path('home/', include('apps.home.urls')),

    path('', include(apps.get_app_config('oscar').urls[0])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

