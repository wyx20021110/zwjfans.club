from django.urls import path
from zwjweb.views.index import index

urlpatterns = [
    path('', index, name='index'),


]
