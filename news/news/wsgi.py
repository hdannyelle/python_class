"""
WSGI config for news project.

"""
#created when running the startproject command to set up default
#WSGI configuration

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

application = get_wsgi_application()
