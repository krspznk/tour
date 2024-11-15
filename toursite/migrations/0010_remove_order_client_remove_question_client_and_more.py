# Generated by Django 5.0.2 on 2024-03-25 23:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursite', '0009_alter_excursion_options_client_password1_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='question',
            name='client',
        ),
        migrations.RemoveField(
            model_name='tourorder',
            name='client',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tourorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tour_orders_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
