# Generated by Django 3.2.18 on 2023-03-19 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0011_alter_userprofileimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileimage',
            old_name='image',
            new_name='profile_image',
        ),
    ]