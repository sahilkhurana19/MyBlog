from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    desc_sh = models.TextField(verbose_name = 'Short Description')
    desc_lg = models.TextField(verbose_name = 'Long Description')
    create_date = models.DateTimeField(verbose_name = 'Created on:', default = now)
    published_date = models.DateTimeField(verbose_name = 'Published on:', blank = True, null =  True)
    read_time = models.IntegerField(default = 5)

    def publish():
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return "%s" % (self.title)

class Tag(models.Model):
    parent = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = 'Post')
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return "%s" % (self.name)