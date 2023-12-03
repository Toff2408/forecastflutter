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

    def __str__(self):
        return self.league


class Team(models.Model):
    name = models.CharField(max_length=150)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Headtohead(models.Model):
    
    team = models.ManyToManyField(Team)
    g1 = models.CharField(max_length=1, default='W')
    g2 = models.CharField(max_length=1, default='W')
    g3 = models.CharField(max_length=1, default='W')
    g4 = models.CharField(max_length=1, default='W')
    g5 = models.CharField(max_length=1, default='W')

    def __str__(self):
        return self.g1


class Game(models.Model):
    headhead = models.ForeignKey(Headtohead, on_delete=models.CASCADE, null=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team', null=True, blank=True)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team', null=True, blank=True)
    # g_country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True, blank=True)
    # g_league = models.ForeignKey(League,on_delete=models.CASCADE,related_name='leagues')
    date = models.TimeField()
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    to_win = models.IntegerField(default=1)
    goals = models.CharField(max_length=1)
    result = models.BooleanField(null=True, blank=True)
<<<<<<< HEAD
    lastfive_home = models.CharField(max_length=5, default='LLLLL')
    lastfive_away = models.CharField(max_length=5, default='WWWWW')

=======
    last_fivehome = models.CharField(max_length=5, default='LLLLL')
    last_fiveaway = models.CharField(max_length=5, default='LLLLL')
>>>>>>> master

    def __str__(self):
        return str(self.home_team) + ' - ' + str(self.away_team)
