from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



class Driver(AbstractUser):
    license_number = models.CharField(unique=True)

    class Meta:
        ordering = ("license_number",)
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ("name",)
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ("model",)
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self) -> str:
        return self.model
