import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bennuofficial.settings")

application = get_wsgi_application()

# Settings for Application Deployment to Heroku
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
