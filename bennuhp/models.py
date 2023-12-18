import uuid

from django.db import models


class Music(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(blank=True, null=True)
    descriptions = models.TextField(null=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class Movie(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    venue = models.TextField()
    descriptions = models.TextField(null=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class LiveSchedule(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
