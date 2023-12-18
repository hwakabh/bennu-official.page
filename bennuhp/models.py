from django.db import models
# from django.utils import timezone


class Music(models.Model):
    uuid = models.UUIDField()
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(blank=True, null=True)
    descriptions = models.TextField(null=True)
    url = models.URLField()

    def _str__(self):
        return self.title


class Movie(models.Model):
    uuid = models.UUIDField()
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    venue = models.TextField()
    descriptions = models.TextField(null=True)
    url = models.URLField()

    def _str__(self):
        return self.title


class LiveSchedule(models.Model):
    uuid = models.UUIDField()
