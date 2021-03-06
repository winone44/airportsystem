# Generated by Django 4.0.3 on 2022-04-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_planeflights_gate_planeflights_terminal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeflights',
            name='status',
            field=models.IntegerField(choices=[('0', 'Cancelled'), ('1', 'Scheduled'), ('2', 'Scheduled Delayed'), ('3', 'Go to your gate'), ('4', 'Last call'), ('5', 'En Route'), ('6', 'En Route Delayed'), ('7', 'Landed'), ('8', 'Landed Delayed')], default='1'),
        ),
    ]
