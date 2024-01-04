from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('biography/', views.biography, name='bio'),
    path('discography/', views.discograpth, name='disco'),
    path('lives/', views.lives, name='live'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
