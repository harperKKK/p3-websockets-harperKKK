# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('initial/', views.initial, name='initial'),
    path('main/', views.main, name='main'),
    path('onefeed/', views.onefeed, name='onefeed'),
    path('tabs/', views.tabs, name='tabs'),
    path('large/', views.large, name='large'),
]

