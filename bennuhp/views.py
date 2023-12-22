from django.shortcuts import render

from bennuhp.models.music import Music
from bennuhp.models.movie import Movie
from bennuhp.models.liveschedule import LiveSchedule


def home(request):
    for r in request.GET:
        print(r)
    return render(request, 'bennuhp/home.html', {})


def biography(request):
    return render(request, 'bennuhp/biography.html', {})


def discograpth(request):
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


def page_not_found(request):
    return render(request, 'bennuhp/common/page_not_found.html', {})
