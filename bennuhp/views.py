from django.shortcuts import render
from bennuhp.models import BlogPost


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def biography(request):
    return render(request, 'biography.html', {})


def discograpth(request):
    return render(request, 'discography.html', {})


def lives(request):
    return render(request, 'lives.html', {})


def page_not_found(request):
    return render(request, 'page_not_found.html', {})
