from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


# Requires for tests
app_name = 'bennuhp'

urlpatterns = [
    path('healthz', views.HealthzView.as_view(), name='healthz'),
    path('home/', views.AppRootTemplateView.as_view(), name='root'),
    path('biography/', views.BioTemplateView.as_view(), name='bio'),
    path('discography/', views.DiscoListView.as_view(), name='disco'),
    path('lives/', views.LivesListView.as_view(), name='live'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
