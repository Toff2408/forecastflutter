from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    # league = League.objects.all().order_by('l_country')#queryset for all country/ order_by to arrange alphabetically#
    games = Games.objects.all().order_by('g_league')
    context = {
        "games":games
    }
    return render(request, 'index.html', context)