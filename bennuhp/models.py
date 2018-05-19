from django.db import models
from django.utils import timezone


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)


    def publish_post(self):
        self.publish_date = timezone.now()
        self.save()

    # Python Internal Method.
    def _str__(self):
        return self.title

