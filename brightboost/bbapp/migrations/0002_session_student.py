# Generated by Django 4.2.5 on 2023-10-25 01:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='student',
            field=models.ManyToManyField(default=None, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
