from django.contrib import admin
from .models import Airport, Flight, Passanger

# Register your models here.
admin.site.register(Flight)


class FlightAdminInline(admin.TabularInline):
    model = Flight
    fk_name = "origin"
    extra = 3


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    inlines = [FlightAdminInline]


@admin.register(Passanger)
class PassangerAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ('first_name', 'last_name')
    }
