# Generated by Django 5.0.2 on 2024-03-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursite', '0007_alter_tour_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursion',
            options={'verbose_name_plural': 'Excursion'},
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tour',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tour',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='tourorder',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transpont',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
