# Generated by Django 4.2.7 on 2023-12-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0030_gamedates_game_gamedates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedates',
            name='dates',
            field=models.DateField(),
        ),
    ]