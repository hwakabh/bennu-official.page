# Generated by Django 5.0 on 2024-01-16 11:23

import django_mysql.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveSchedule',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('descriptions', models.TextField(null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('venue', models.TextField()),
                ('url', models.URLField()),
                ('open_time', models.TimeField(null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('with_actors', django_mysql.models.ListCharField(models.CharField(blank=True, default='', max_length=20), max_length=210, size=10)),
                ('image_path', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('venue', models.TextField()),
                ('descriptions', models.TextField(null=True)),
                ('url', models.URLField()),
                ('image_path', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('descriptions', models.TextField(null=True)),
                ('url', models.URLField()),
                ('image_path', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
    ]
