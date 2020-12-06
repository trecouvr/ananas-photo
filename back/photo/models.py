from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db import models as gis_models


class User(AbstractUser):
    pass


class Folder(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        related_query_name='children',
    )


class Tag(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='tags',
        related_query_name='tags',
    )


class Picture(models.Model):
    name = models.CharField(max_length=128)
    s3_key = models.CharField(max_length=512)
    folder = models.ForeignKey(
        Folder,
        on_delete=models.PROTECT,
        related_name='pictures',
        related_query_name='pictures',
    )
    datetime = models.DateTimeField()
    location = gis_models.PointField(geography=True)
