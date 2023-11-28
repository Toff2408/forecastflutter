from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    games = Game.objects.all().order_by('home_team__league')
    print(games)
    context = {
        "games": games,
    }

    return render(request, 'index.html', context)
