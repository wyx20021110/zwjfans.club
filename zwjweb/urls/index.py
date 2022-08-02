from django.urls import path
from zwjweb.views.index import index
from zwjweb.views.game import game

urlpatterns = [
    path('', index, name='index'),
    path('game/', game, name="game"),


]
