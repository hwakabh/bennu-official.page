from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views


# Requires for tests
app_name = 'bennuhp'

urlpatterns = [
    re_path('healthz', views.HealthzView.as_view(), name='healthz'),
    re_path('biography/', views.BioTemplateView.as_view(), name='bio'),
    re_path('discography/', views.DiscoListView.as_view(), name='disco'),
    re_path('lives/', views.LivesListView.as_view(), name='live'),
    re_path(r'^$', views.AppRootTemplateView.as_view(), name='root'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
