# Generated by Django 4.2 on 2023-04-20 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0009_capturedanimal_capturedanimal_unique_ownership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desired_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desired_in_trades', to='is_it_raining.capturedanimal')),
                ('offered_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offered_in_trades', to='is_it_raining.capturedanimal')),
                ('trade_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_trades', to=settings.AUTH_USER_MODEL)),
                ('trade_starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiated_trades', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
