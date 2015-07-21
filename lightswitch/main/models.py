from django.db import models


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    logoff_ts = models.DateTimeField(null=True)
    join_ts = models.DateTimeField(null=True)
    ship = models.ForeignKey('main.Ship', null=True)
    location = models.ForeignKey('main.Location', null=True)

    def __unicode__(self):
        return self.name


class Ship(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.name
