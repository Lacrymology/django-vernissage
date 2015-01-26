"""
Models for gallery
"""

import json

from django.db import models
from filer.fields.image import FilerImageField

from vernissage import settings as vsets

class Image(models.Model):
    """
    Image objects for the galleries
    """
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    image = FilerImageField(related_name="gallery_image")
    alt = models.CharField(max_length=128)
    gallery = models.ForeignKey('vernissage.Gallery')

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order',)

class Gallery(models.Model):
    """
    Gallery model
    """
    title = models.CharField(max_length=64)
    attributes = models.TextField(default=json.dumps(
        vsets.VERNISSAGE_GALLERY_ATTRIBUTES))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Galleries'
