# Generated by Django 4.2.5 on 2023-10-06 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_youtube',
        ),
    ]