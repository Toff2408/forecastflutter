# Generated by Django 4.2.7 on 2023-11-16 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0014_alter_league_l_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='l_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccergames.country'),
        ),
    ]