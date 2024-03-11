from django.contrib import admin
from .models import Location, Server, VirtualServer, TransportUnit, PowerUnit


# Base admin class defining common settings for device-related admin panels.
class BaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'status', 'get_location_user']
    list_filter = ['status', 'location__user']
    ordering = ['name', 'location', 'status']
    raw_id_fields = ['location']
    search_fields = ['name', 'location__name', 'status']

    def get_location_user(self, obj):
        return obj.location.user
    get_location_user.short_description = 'User'


# Admin panel configuration for the Location model.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'county', 'city', 'district', 'user']
    list_filter = ['county', 'user']
    ordering = ['name', 'county', 'city', 'district']
    raw_id_fields = ['user']
    search_fields = ['name', 'county', 'city', 'district']
    

# Admin panel configuration for the Server model, inheriting from BaseAdmin.
@admin.register(Server)
class ServerAdmin(BaseAdmin):
    pass


@admin.register(VirtualServer)
class VirtualServerAdmin(BaseAdmin):
    list_display = ['name', 'host_server', 'location', 'status', 
                    'get_location_user']
    list_filter = ['status', 'host_server__location__user']
    ordering = ['name', 'host_server', 'status']
    raw_id_fields = ['host_server']
    search_fields = ['name', 'host_server__name', 
                     'host_server__location__name', 'status']


@admin.register(TransportUnit)
class TransportUnitAdmin(BaseAdmin):
    pass


@admin.register(PowerUnit)
class PowerUnitAdmin(BaseAdmin):
    pass
