from django.contrib import admin

from .models import Service, ServiceObject, Settings, TankReading

class ServiceObjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    fields = ["name", "description"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "service_object", "description", "created"]


class SettingsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "value"]


class TankReadingAdmin(admin.ModelAdmin):
    list_display = ["id", "reading", "action", "created"]


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceObject, ServiceObjectAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(TankReading, TankReadingAdmin)
