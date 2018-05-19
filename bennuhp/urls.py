from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^home/', views.home),
    url(r'^biography/', views.biography),
    url(r'^discography/', views.discograpth),
    url(r'^lives/', views.lives),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)