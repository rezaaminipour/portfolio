import os
import sys

from django.apps import AppConfig
from django.core.management import call_command


class PortfolioConfig(AppConfig):
    name = 'portfolio'

    def ready(self):
        # On hosts whose start command does not run `migrate` (e.g. Render),
        # apply migrations automatically at startup so the DB is ready.
        if 'migrate' in sys.argv or 'makemigrations' in sys.argv:
            return
        if os.environ.get('RENDER') or 'runserver' in sys.argv:
            try:
                call_command('migrate', interactive=False, verbosity=0)
            except Exception:
                pass
