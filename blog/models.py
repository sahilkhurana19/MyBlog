from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    desc_sh = RichTextUploadingField(verbose_name = 'Short Description')
    desc_lg = RichTextUploadingField(verbose_name = 'Long Description')
    create_date = models.DateTimeField(verbose_name = 'Created on:', default = timezone.now())
    published_date = models.DateTimeField(verbose_name = 'Published on:', blank = True, null =  True)
    read_time = models.IntegerField(default = 5)

    def was_published_recently(self):
        now  = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now
    was_published_recently.admin_order_field = 'published_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return "%s" % (self.title)

class Tag(models.Model):
    parent = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = 'Post')
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return "%s" % (self.name)