from django.db import models

# Create your models here.
class Album(models.Model):
    name=models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    slug=models.SlugField()


class Track(models.Model):
    name=models.CharField(max_length=10)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField()