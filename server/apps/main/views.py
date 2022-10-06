"""Views for main project's app."""

from django.views import generic


class IndexView(generic.TemplateView):
    """Generic view for index template."""

    template_name = 'main/index.html'
