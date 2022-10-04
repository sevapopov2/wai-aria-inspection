"""Django-split-settings main configuration file."""

from os import environ

import django_stubs_ext

from split_settings.tools import include


# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()

# Managing environment via `DJANGO_ENV` variable:
environ.setdefault('DJANGO_ENV', 'development')
_current_env = environ['DJANGO_ENV']

_base_settings = (
    'components/common.py',
    'components/database.py',
    'components/ui.py',
    # Select the right env:
    'environments/{0}.py'.format(_current_env),
)

include(*_base_settings)
