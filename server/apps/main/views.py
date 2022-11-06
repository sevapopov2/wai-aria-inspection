"""Views for main project's app."""

from django.views import generic


class IndexView(generic.TemplateView):
    """Generic view for main index template."""

    template_name = 'main/index.html'


class BadMenuExampleView(generic.TemplateView):
    """Bad menu example view."""

    template_name = 'main/bad-examples/menu.html'


class BrokenSemanticsBadExample(generic.TemplateView):
    """View for fixing broken semantics with ARIA bad example."""

    template_name = 'main/bad-examples/broken-semantics.html'


class RedundantSemanticsBadExample(generic.TemplateView):
    """A generic view for reduntant semantics bad example."""

    template_name = 'main/bad-examples/redundant-semantics.html'


class GoodMenuExampleView(generic.TemplateView):
    """Good menu example generic view."""

    template_name = 'main/good-examples/menu.html'


class BrokenSemanticsGoodExample(generic.TemplateView):
    """Fixing broken semantics generic view."""

    template_name = 'main/good-examples/fixing-broken-semantics.html'


class RedundantSemanticsGoodExample(generic.TemplateView):
    """A generic view for fixing redundant semantics example."""

    template_name = 'main/good-examples/fixing-redundant-semantics.html'
