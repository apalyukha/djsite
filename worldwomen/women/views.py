from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = ["Про сайт", "Добавити статтю", "Зворотній зв'язок", "Login"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Головна сторінка'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Про сайт'})


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
