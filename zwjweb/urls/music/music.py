from django.urls import path
from zwjweb.views.music.music import music

urlpatterns = [
    path('', music, name="music"),
]
