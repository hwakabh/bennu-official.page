from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from bennuhp.views import NotFoundTemplateView, ServerErrorTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bennuhp.urls')),
]

# note that Applicable only in DEBUG = False
handler404 = NotFoundTemplateView.as_view()
handler500 = ServerErrorTemplateView.as_view()
