from django.db import models

# Create your models here.
class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return (u"%s %s" % self.latitude, self.longitude)

class Device(models.Model):
    location = models.ForeignKey(Location)
    name = models.CharField(max_length=75)

    devID = models.IntegerField()

    def __unicode__(self):
        return (u"$s - %s - %s" % self.name, self.devID, self.location)

