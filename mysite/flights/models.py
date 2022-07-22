from django.db import models
from django.utils.timezone import now


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
    created_at = models.DateTimeField(verbose_name="Дата создания", default=now)

    def __str__(self):
        return f"{self.origin} в {self.destination}. Длительность - {self.duration} часов"

    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0

class Passanger(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    flight = models.ManyToManyField(Flight, related_name="passangers", blank=True)
    slug = models.SlugField(verbose_name="ЧПУ", blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Пассажир"
