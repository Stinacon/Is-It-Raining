# Generated by Django 4.2 on 2023-04-18 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0004_remove_weather_temp_weather_weather_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='owner',
        ),
    ]