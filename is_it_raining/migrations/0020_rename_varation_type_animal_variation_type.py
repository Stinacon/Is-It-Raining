# Generated by Django 4.2 on 2023-04-26 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0019_animal_varation_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='varation_type',
            new_name='variation_type',
        ),
    ]
