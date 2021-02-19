from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("<h1>women...</h1>")


def categories(request, catid):
    return HttpResponse(f"<h1>Список...</h1><p>{catid}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Історія архіву ...</h1><p>{year}</p>")
