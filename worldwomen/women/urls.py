from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),  # http://127.0.0.1:8000/women/
    path('cat/<int:catid>/', categories),  # http://127.0.0.1:8000/cat/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)  # http://127.0.0.1:8000/archive/2021/
]
