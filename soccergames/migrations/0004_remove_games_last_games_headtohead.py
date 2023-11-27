# Generated by Django 4.2.7 on 2023-11-20 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0003_games_away_team_games_home_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='last_games',
        ),
        migrations.CreateModel(
            name='Headtohead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.CharField(max_length=1)),
                ('draw', models.CharField(max_length=1)),
                ('lost', models.CharField(max_length=1)),
                ('ht_team1', models.ForeignKey(on_delete=django.db.models.deletion.SET, related_name='ht_team1', to='soccergames.team')),
            ],
        ),
    ]