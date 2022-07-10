from django.db import models


# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя аэропорта")
    city = models.CharField(max_length=100, verbose_name="Имя города")

    def __str__(self):
        return self.name
