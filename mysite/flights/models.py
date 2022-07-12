from django.db import models


# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя аэропорта")
    city = models.CharField(max_length=100, verbose_name="Имя города")

    def __str__(self):
        return f"{self.name} {self.city}"

    def get_arivals(self):
        return self.flights_destination.all()


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flights_origin", verbose_name="Место отбытия")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flights_destination", verbose_name="Место прибытия")
    duration = models.IntegerField(verbose_name="Длительность")

    def __str__(self):
        return f"{self.origin} в {self.destination}. Длительность - {self.duration} часов"
