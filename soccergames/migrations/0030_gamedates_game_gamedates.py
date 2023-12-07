# Generated by Django 4.2.7 on 2023-12-07 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0029_game_headhead'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='gamedates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soccergames.gamedates'),
        ),
    ]
