# Generated by Django 4.0.3 on 2022-04-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planeflights',
            name='carrier',
            field=models.CharField(default='LOT', max_length=200),
        ),
    ]
