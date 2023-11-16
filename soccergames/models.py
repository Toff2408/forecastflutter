from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Country(models.Model):
    country = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Country',null=True, blank=True)

    def __str__(self):
        return self.country


class League(models.Model):
    l_country = models.ForeignKey(Country,on_delete=models.CASCADE)
    league = models.CharField(max_length=200)
    
    def __str__(self):
        return self.league


class Games(models.Model):
    LASTGAMES = [
        ('W','WIN'),
        ('D','DRAW'),
        ('L','LOSE'),
    ]
    g_country = models.ForeignKey(Country,on_delete=models.CASCADE)
    g_league = models.ForeignKey(League,on_delete=models.CASCADE)
    time = models.TimeField(null=True)
    last_games = models.CharField(max_length=5,choices=LASTGAMES)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    to_win = models.IntegerField(default=1)
    goals = models.CharField(max_length=1)
    result = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.last_games

