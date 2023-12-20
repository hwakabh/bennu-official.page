from django.contrib import admin

from bennuhp.models.music import Music
from bennuhp.models.movie import Movie
from bennuhp.models.liveschedule import LiveSchedule

# To handle in Django administration site
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(LiveSchedule)
