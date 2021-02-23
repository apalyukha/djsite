from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("<h1>women...</h1>")


def categories(request, catid):
    if (request.GET):
        print(request.GET)  # http://127.0.0.1:8000/cat/1/?name=GalGadot&type==actress

    # if (request.POST):
    #     print(request.POST)

    return HttpResponse(f"<h1>Список...</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2021:
        # raise Http404
        return redirect('home', permanent=False)
    # http://127.0.0.1:8000/archive/2021/
    return HttpResponse(f"<h1>Історія архіву ...</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено ...</h1>')
