from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img')


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'league','slug')
    prepopulated_fields = {'slug':('league',)}


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'league',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id','home_team','away_team','gamedates',  'date', 'home_odd','draw_odd','away_odd', 'to_win', 'goals', 'result','lastfive_home','lastfive_away','won','notwon','overone','overtwo','overthree')


@admin.register(Headtohead)
class HeadtoheadAdmin(admin.ModelAdmin):
    list_display = ('id','first_team','second_team','result','date')

@admin.register(GameDates)
class GameDatesAdmin(admin.ModelAdmin):
    list_display = ('id','dates')


