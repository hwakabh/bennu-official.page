from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home),
    url(r'^biography/', views.biography),
    url(r'^discography/', views.discograpth),
    url(r'^lives/', views.lives),
]

