# Generated by Django 4.2.7 on 2023-11-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0016_games'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='to_win',
            field=models.IntegerField(default=1),
        ),
    ]
