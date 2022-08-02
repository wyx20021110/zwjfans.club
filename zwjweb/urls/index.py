from django.urls import path, include
from zwjweb.views.index import index

urlpatterns = [
    path('', index, name='index'),
    path('game/', include('zwjweb.views.game.game')),


]
