# Generated by Django 5.0.2 on 2024-03-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursite', '0011_remove_tourorder_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_image',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
