from django.shortcuts import render
from .models import *
from datetime import date



def index(request):
    format = date.today()
    games = Game.objects.all().order_by('home_team__league').filter(gamedates__dates=format)
    premier = League.objects.all().order_by('league')
    
    context = {
        "games": games,
        "premier":premier
    }

    return render(request, 'index.html', context)

def detail(request, id, slug):
    details = Game.objects.get(pk = id)
    head = Headtohead.objects.get(pk=1)
   
    context = {
        "details":details,
        "head":head
    }
                    
    return render(request, 'detail.html', context)

# def indexx(request):
#     premier = Game.objects.filter(premier="premier")
    
#     context = {
#         "premier": premier,
#     }
#     return render(request, "index.html", context)


# def indexx(request):
#     premier = Game.objects.filter(headhead__first_team__league='league')
    
#     context = {
#         "premier": premier,
#     }
#     return render(request, "index.html", context)

# def indexx(request):
#     premier = Product.objects.filter(category__title= title)
#     premier = Date.objects.filter(category__title= title)
    
#     context = {
#         "premier": premier,
#     }
#     return render(request, "index.html", context)