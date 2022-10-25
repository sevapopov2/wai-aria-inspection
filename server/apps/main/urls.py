"""Main app's urls configuration."""

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(),
         name='index'),
    path('bad-examples/menu', views.BadMenuExampleView.as_view(),
         name='bad-menu-example'),
    path('bad-examples/broken-semantics',
         views.BrokenSemanticsBadExample.as_view(),
         name='broken-semantics-bad-example'),
    path('bad-examples/redundant-semantics',
         views.RedundantSemanticsBadExample.as_view(),
         name='redundant-semantics-bad-example'),
    path('good-examples/menu', views.GoodMenuExampleView.as_view(),
         name='good-menu-example'),
    path('good-examples/broken-semantics',
         views.BrokenSemanticsGoodExample.as_view(),
         name='broken-semantics-good-example'),
    path('good-examples/redundant-semantics',
         views.RedundantSemanticsGoodExample.as_view(),
         name='redundant-semantics-good-example')
]
