from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^home/', views.home, name='hm'),
    url(r'^biography/', views.biography, name='bio'),
    url(r'^discography/', views.discograpth, name='dsk'),
    url(r'^lives/', views.lives, name='lv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)