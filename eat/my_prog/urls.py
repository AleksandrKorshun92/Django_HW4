from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('cub/', views.cub, name='cub'),
    path('random_number/', views.random_number, name='random_number'),
    path('about/', views.about, name='about'),
]
