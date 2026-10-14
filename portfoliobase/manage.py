#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfoliobase.settings')

    args = sys.argv
    is_runserver = 'runserver' in args
    port = os.environ.get('PORT')
    on_render = bool(os.environ.get('RENDER'))

    # Render (and similar hosts) require the server to bind to 0.0.0.0:$PORT.
    if is_runserver and port:
        has_addr = any(
            a.startswith(('0.0.0.0', '127.0.0.1', 'localhost', '[::]'))
            for a in args
        )
        if not has_addr:
            args = args + [f'0.0.0.0:{port}']

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Apply migrations before starting the dev server on Render.
    if on_render and is_runserver:
        import django

        django.setup()
        from django.core.management import call_command

        try:
            call_command('migrate', interactive=False, verbosity=0)
        except Exception:
            pass

    execute_from_command_line(args)


if __name__ == '__main__':
    main()
