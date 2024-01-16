import uuid

from django.db import models
from django_mysql.models import ListCharField


class LiveSchedule(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(max_length=200)
    descriptions = models.TextField(null=True)
    date = models.DateField(
        null=True,
        blank=True,
    )
    venue = models.TextField()
    url = models.URLField()

    open_time = models.TimeField(null=True)
    start_time = models.TimeField(
        null=True,
        blank=True,
    )
    price = models.IntegerField(
        null=True,
        blank=True,
    )

    with_actors = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=''),
        size=10,
        max_length=(21 * 10),
    )

    image_path = models.CharField(
        max_length=200,
        blank=True,
        default=''
    )


    def __str__(self):
        return self.title
