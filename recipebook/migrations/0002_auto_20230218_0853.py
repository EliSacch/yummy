# Generated by Django 3.2.18 on 2023-02-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
