"""
WSGI config for EasyAid project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyAid.settings')

application = get_wsgi_application()
# Удалите строку с WhiteNoise - media файлы и так будут обслуживаться в DEBUG режиме