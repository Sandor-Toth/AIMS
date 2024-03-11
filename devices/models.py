from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    county = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self) -> str:
        return self.name


class BaseDevice(models.Model):
    STATUS = {
        'D': 'DOWN',
        'I': 'IDLE',
        'W': 'WORK',
    }
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class Server(BaseDevice):
    location = models.ForeignKey(Location,
                                 related_name='server_locations',
                                 on_delete=models.PROTECT)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]


class VirtualServer(BaseDevice):
    host_server = models.ForeignKey(Server, 
                                    related_name='virtual_servers', 
                                    on_delete=models.PROTECT)
    @property
    def location(self):
        return self.host_server.location
    
    class Meta:
        ordering = ['name']
        db_table = 'virtual_server'
        indexes = [
            models.Index(fields=['name']),
        ]


class TransportUnit(BaseDevice):
    location = models.ForeignKey(Location,
                                 related_name='transportunit_locations',
                                 on_delete=models.PROTECT)
    class Meta:
        ordering = ['name']
        db_table = 'transport_unit'
        indexes = [
            models.Index(fields=['name']),
        ]


class PowerUnit(BaseDevice):
    location = models.ForeignKey(Location,
                                 related_name='powerunit_locations',
                                 on_delete=models.PROTECT)
    class Meta:
        ordering = ['name']
        db_table = 'power_unit'
        indexes = [
            models.Index(fields=['name']),
        ]
