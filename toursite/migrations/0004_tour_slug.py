# Generated by Django 5.0.2 on 2024-03-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursite', '0003_tour_tour_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
