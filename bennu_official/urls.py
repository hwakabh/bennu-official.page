from django.contrib import admin
from django.conf.urls import include, handler404
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# from bennuhp.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bennuhp.urls')),
]

handler404 = 'bennuhp.views.page_not_found'

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
