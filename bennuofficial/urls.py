from django.contrib import admin
from django.conf.urls import include, url

from bennuhp.views import page_not_found

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^bennu/', include('bennuhp.urls')),
    url(r'^', page_not_found),
]
