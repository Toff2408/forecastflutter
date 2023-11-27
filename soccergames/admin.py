from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img')


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'league',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'league', 'name',)


@admin.register(Games)
class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'home_team', 'away_team', 'time', 'home_odd', 'draw_odd', 'away_odd', 'to_win', 'goals', 'result',)


@admin.register(Headtohead)
class HeadtoheadAdmin(admin.ModelAdmin):
    list_display = ('g1', 'g2', 'g3', 'g4', 'g5')
