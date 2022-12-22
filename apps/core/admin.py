from django.contrib import admin

from .models import Group, CentralGovernment, Time, Manager, Actions, Resource, MapLocation


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(CentralGovernment)
class CentralGovernmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['year', 'timer', 'start_time', 'active']


@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ['title_fa', 'consumption_water', 'consumption_food', 'consumption_fuel',
                    'consumption_gold', 'consumption_ap']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_fa', 'image']


@admin.register(MapLocation)
class MapLocationAdmin(admin.ModelAdmin):
    list_display = ['location_title', 'weather', ]
