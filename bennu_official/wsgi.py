import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bennu_official.settings")

application = get_wsgi_application()

# adding alias for Vercel deployment
# https://vercel.com/templates/python/django-hello-world
app = application
