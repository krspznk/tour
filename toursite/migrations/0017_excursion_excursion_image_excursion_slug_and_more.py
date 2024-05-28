# Generated by Django 5.0.2 on 2024-03-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursite', '0016_alter_hotel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='excursion_image',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='excursion',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='transpont',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='transpont',
            name='transport_image',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
