# Generated by Django 4.0.4 on 2022-06-22 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0032_remove_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.OneToOneField(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
