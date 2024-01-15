from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from bennuhp.models.music import Music
from bennuhp.models.movie import Movie
from bennuhp.models.liveschedule import LiveSchedule


class HealthzView(View):
    def get(self, request):
        return JsonResponse(
            data={
                "status": "ok"
            },
            status=200
        )


def home(request):
    for r in request.GET:
        print(r)
    return render(request, 'bennuhp/home.html', {})


def biography(request):
    return render(request, 'bennuhp/biography.html', {})


def discography(request):
    musics = Music.objects.all()
    movies = Movie.objects.all()
    return render(
        request,
        'bennuhp/discography.html',
        {
            "musics": musics,
            "movies": movies
        }
    )


def lives(request):
    lives = LiveSchedule.objects.all()
    return render(
        request,
        'bennuhp/lives.html',
        {
            "lives": lives
        }
    )


def page_not_found(request, exception):
    return render(
        request,
        'bennuhp/common/page_not_found.html',
        {},
        status=404
    )
