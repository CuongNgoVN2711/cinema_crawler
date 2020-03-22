from django.db import models
from django.utils import timezone
import json


# Create your models here.
class ScrapedMovieItem(models.Model):
    id = models.AutoField(primary_key=True)
    # unique_id = models.CharField(max_length=100, n)
    data = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    @property
    def to_dict(self):
        ret = {
            'data': json.load(self.data),
            'date': self.date
        }
        return ret

    def __str__(self):
        return "Item {}".format(self.id)


class ResourceURL(models.Model):
    site_name = models.CharField(primary_key=True, max_length=20)
    url = models.URLField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.site_name, self.url)
