# Generated by Django 3.2.18 on 2023-03-20 18:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0012_rename_image_userprofileimage_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='procedure',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=200), blank=True, null=True, size=None),
        ),
    ]