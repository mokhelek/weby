# Generated by Django 4.0.4 on 2022-06-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_profile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
