"""Global project's URL Configuration."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('server.apps.main.urls')),
    path('admin/', admin.site.urls),
]
