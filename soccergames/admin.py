from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','country','img',)

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id','l_country','league',)

@admin.register(Games)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id','g_country','g_league','time','last_games','home_team','away_team','home_odd','draw_odd','away_odd','to_win','goals','result',)
