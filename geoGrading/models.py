from django.db import models


class Event(models.Model):
    event_Id = models.IntegerField()
    matched = models.CharField(max_length=200)
    asciiname = models.CharField(max_length=200)
    feature = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    event_text = models.CharField(max_length=200)
    target = models.CharField(max_length=200)

    def __str__(self):
        return str(self.event_Id) + " " + self.asciiname

    def natural_key(self):
        return(self.event_Id)

class TrueLocation(models.Model):
    event = models.ForeignKey(Event)
    location = models.CharField(max_length=200)
