"""Views for main project's app."""

from django.views import generic


class IndexView(generic.TemplateView):
    """Generic view for main index template."""

    template_name = 'main/index.html'


class GoodExamplesIndexView(generic.TemplateView):
    """Generic good examples index view."""

    template_name = 'main/good-examples/index.html'


class BadExamplesIndexView(generic.TemplateView):
    """Generic bad examples index view."""

    template_name = 'main/bad-examples/index.html'
