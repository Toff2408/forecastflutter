# Generated by Django 4.2.7 on 2023-11-20 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0005_remove_headtohead_draw_remove_headtohead_ht_team1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='headtohead',
        ),
    ]
