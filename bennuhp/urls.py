from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home/', views.home, name='hm'),
    path('biography/', views.biography, name='bio'),
    path('discography/', views.discograpth, name='dsk'),
    path('lives/', views.lives, name='lv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
