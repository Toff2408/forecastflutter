from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Country', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class League(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    league = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.league




class Team(models.Model):
    name = models.CharField(max_length=150)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Headtohead(models.Model):
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='firstteam',null=True, blank=True)
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='secondteam',null=True, blank=True)
    result = models.CharField(max_length=100, null=True,blank=True)
    date = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.first_team)

class GameDates(models.Model):
    # game = models.ForeignKey('Game', on_delete=models.CASCADE)
    # date = models.DateTimeField(default=datetime.now())
    # dates = models.DateField(widget=dates(format='%d-%m-%Y'), 
    #                    input_formats=['%d-%m-%Y'])
    dates = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.dates) 


class Game(models.Model):
    gamedates = models.ForeignKey(GameDates, on_delete=models.CASCADE, null=True, blank=True)
    headhead = models.ForeignKey(Headtohead, on_delete=models.CASCADE,null=True,blank=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team', null=True, blank=True)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team', null=True, blank=True)
    date = models.TimeField()
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    to_win = models.IntegerField(default=1)
    goals = models.CharField(max_length=1)
    result = models.BooleanField(null=True, blank=True)
    lastfive_home = models.CharField(max_length=5, default='LLLLL')
    lastfive_away = models.CharField(max_length=5, default='WWWWW')
    won = models.CharField(max_length=100, null=True,blank=True)
    notwon = models.CharField(max_length=100,null=True,blank=True)
    overone = models.BooleanField(null=True, blank=True)
    overtwo = models.BooleanField(null=True, blank=True)
    overthree = models.BooleanField(null=True, blank=True)


    def __str__(self):
        return str(self.home_team) + ' - ' + str(self.away_team)

    
