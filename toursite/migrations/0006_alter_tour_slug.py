# Generated by Django 5.0.2 on 2024-03-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursite', '0005_alter_tour_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
