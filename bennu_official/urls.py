from django.contrib import admin
from django.conf.urls import include, handler404
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bennuhp.urls')),
]

# note that Applicable only in DEBUG = False
handler404 = 'bennuhp.views.page_not_found'
