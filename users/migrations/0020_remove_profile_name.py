# Generated by Django 4.0.4 on 2022-06-22 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
