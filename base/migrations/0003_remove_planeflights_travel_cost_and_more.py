# Generated by Django 4.0.3 on 2022-04-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_planeflights_carrier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planeflights',
            name='travel_cost',
        ),
        migrations.AlterField(
            model_name='planeflights',
            name='carrier',
            field=models.CharField(max_length=200),
        ),
    ]
