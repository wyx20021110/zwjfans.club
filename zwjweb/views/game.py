from django.shortcuts import render


def game(request):
    return render(request, 'game/cxk-ball-hitplane/index.html')
