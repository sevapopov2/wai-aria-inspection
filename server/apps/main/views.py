"""Views for main project's app."""

from django.views import generic


class IndexView(generic.TemplateView):
    """Generic view for main index template."""

    template_name = 'main/index.html'


class GoodExamplesIndexView(generic.TemplateView):
    """Generic good examples index view."""

    template_name = 'main/good-examples/index.html'


class BadMenuExampleView(generic.TemplateView):
    """Bad menu example view."""

    template_name = 'main/bad-examples/menu.html'


class fixingBrokenSemanticsExample(generic.TemplateView):
    """View for fixing broken semantics with ARIA example."""

    template_name = 'main/bad-examples/fixing-broken-semantics.html'


class RedundantSemanticsView(generic.TemplateView):
    """A generic view for reduntant semantics bad example."""

    template_name = 'main/bad-examples/redundant-semantics.html'
