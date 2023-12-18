from django.contrib import admin
from django.conf.urls import include
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# from bennuhp.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bennuhp.urls')),
    # url(r'^', page_not_found),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
