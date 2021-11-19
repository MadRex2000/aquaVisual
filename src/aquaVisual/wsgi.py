"""
WSGI config for imbVisual project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from sensorData import mqtt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aquaVisual.settings.local')

application = get_wsgi_application()

mqtt.run()
