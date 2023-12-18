from django.contrib import admin
from .models import Music, Movie, LiveSchedule

# To handle in Django administration site
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(LiveSchedule)
