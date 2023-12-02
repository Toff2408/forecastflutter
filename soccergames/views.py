from django.shortcuts import render
from .models import *



def index(request):
    games = Game.objects.all().order_by('home_team__league')
    context = {
        "games": games
    }

    return render(request, 'index.html', context)

def detail(request):
    return render(request, 'detail.html')
