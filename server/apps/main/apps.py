"""Main app's configurations."""

from django.apps import AppConfig


class MainConfig(AppConfig):
    """Configuration setting app's name and db field langth."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.main'
