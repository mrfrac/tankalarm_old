from django.contrib import admin

from .models import Service, ServiceObject, Settings, TankReading


admin.site.register(Service, admin.ModelAdmin)
admin.site.register(ServiceObject, admin.ModelAdmin)
admin.site.register(Settings, admin.ModelAdmin)
admin.site.register(TankReading, admin.ModelAdmin)
