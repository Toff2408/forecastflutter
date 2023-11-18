from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    leagues = League.objects.all().order_by('league')#queryset for all country/ order_by to arrange alphabetically#
    for item in leagues:
        games = Games.objects.filter(g_league__league = item.league)
    context = {
        "games":games,
        "league":leagues
    }
    
    return render(request, 'index.html', context)