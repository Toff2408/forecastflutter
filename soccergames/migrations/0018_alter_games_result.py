# Generated by Django 4.2.7 on 2023-11-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0017_games_to_win'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='result',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]