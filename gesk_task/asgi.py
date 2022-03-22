"""
ASGI config for gesk_task project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from mqttasgi.consumers import MqttConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gesk_task.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    'mqtt': MqttConsumer,
})
