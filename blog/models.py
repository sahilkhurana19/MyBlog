from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    desc_sh = models.TextField()
    desc_lg = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True, null =  True)
    read_time = models.IntegerField(default = 5)