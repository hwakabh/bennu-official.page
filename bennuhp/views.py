from django.shortcuts import render
from bennuhp.models import BlogPost


def home(request):
    for r in request.GET:
        print(r)
    return render(request, 'bennuhp/home.html', {})


def biography(request):
    return render(request, 'bennuhp/biography.html', {})


def discograpth(request):
    return render(request, 'bennuhp/discography.html', {})


def lives(request):
    return render(request, 'bennuhp/lives.html', {})


def page_not_found(request):
    return render(request, 'bennuhp/common/page_not_found.html', {})
