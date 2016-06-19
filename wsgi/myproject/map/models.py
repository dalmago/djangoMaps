from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=75)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return (self.name)

class Device(models.Model):
    location = models.ForeignKey(Location)
    name = models.CharField(max_length=75)

    devID = models.IntegerField()

    def __str__(self):
        return (self.name)

