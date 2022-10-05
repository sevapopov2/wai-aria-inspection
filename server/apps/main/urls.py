"""Main app's urls configuration."""

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(),
         name='index'),
]
