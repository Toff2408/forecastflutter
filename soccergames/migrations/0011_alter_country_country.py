# Generated by Django 4.2.7 on 2023-11-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccergames', '0010_alter_country_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(default='A', max_length=50),
        ),
    ]
