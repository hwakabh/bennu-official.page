import uuid

from django.db import models
from django_mysql.models import ListCharField

class LiveSchedule(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)
    descriptions = models.TextField(null=True)
    date = models.DateTimeField()
    venue = models.TextField()
    url = models.URLField()

    open_time = models.TimeField(null=True)
    start_time = models.TimeField()
    price = models.IntegerField()
    with_actors = ListCharField(
        base_field=models.CharField(max_length=20)
    )

    def __str__(self):
        return self.title
