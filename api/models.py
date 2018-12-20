from django.db import models


READING_FILL_ACTION = 1
READING_EMPTY_ACTION = 2

TANK_READING_TYPE_CHOICES = [
    (READING_FILL_ACTION, "fill"),
    (READING_EMPTY_ACTION, "empty")
]


class Settings(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "settings"
        verbose_name = "Setting"
        verbose_name_plural = "Settings"


class TankReading(models.Model):
    reading = models.FloatField(default=0)
    action = models.SmallIntegerField(choices=TANK_READING_TYPE_CHOICES, blank=False, null=False, default=READING_FILL_ACTION)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tank_readings"
        ordering = ["-created"]


class ServiceObject(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "service_objects"
        ordering = ["name"]


class Service(models.Model):
    service_object = models.ForeignKey("ServiceObject", on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "service"
        ordering = ["-created"]
