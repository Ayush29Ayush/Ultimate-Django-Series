from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # What type of object is being tagged (eg. product, article)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
