# Generated by Django 5.0 on 2023-12-22 22:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bennuhp', '0004_alter_liveschedule_uuid_alter_movie_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_path',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='image_path',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]