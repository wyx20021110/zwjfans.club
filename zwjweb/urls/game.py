from django.urls import path
from zwjweb.views.game import game

urlpatterns = [
    path('', game, name="game"),
]
