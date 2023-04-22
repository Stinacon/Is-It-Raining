# Generated by Django 4.2 on 2023-04-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0012_animal_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='weather-icons')),
            ],
        ),
    ]
