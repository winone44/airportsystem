# Generated by Django 4.0.3 on 2022-04-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_planeflights_travel_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planeflights',
            name='gate',
            field=models.CharField(default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='planeflights',
            name='terminal',
            field=models.CharField(default='A', max_length=2),
        ),
    ]