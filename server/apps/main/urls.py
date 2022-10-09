"""Main app's urls configuration."""

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(),
         name='index'),
    path('good-examples/', views.GoodExamplesIndexView.as_view(),
         name='good-examples'),
    path('bad-examples/', views.BadExamplesIndexView.as_view(),
         name='bad-examples')
]
