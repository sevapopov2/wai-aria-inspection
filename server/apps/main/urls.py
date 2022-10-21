"""Main app's urls configuration."""

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(),
         name='index'),
    path('good-examples/', views.GoodExamplesIndexView.as_view(),
         name='good-examples'),
    path('bad-examples/menu', views.BadMenuExampleView.as_view(),
         name='bad-menu-example'),
    path('bad-examples/fixing-broken-semantics',
         views.fixingBrokenSemanticsExample.as_view(),
         name='broken-semantics-bad-example'),
    path('bad-examples/redundant-semantics',
         views.RedundantSemanticsView.as_view(), name='redundant-semantics'),
]
