from django.urls import path, include
from zwjweb.views.index import index

urlpatterns = [
    path('', index, name='index'),
    path('game/', include('zwjweb.urls.game.game')),
    path('music/', include('zwjweb.urls.music.music')),
]
