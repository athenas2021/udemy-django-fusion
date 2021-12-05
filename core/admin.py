from django.contrib import admin

from .models import Position, Service, Team

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'status', 'updated')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'status', 'updated')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'status', 'updated')