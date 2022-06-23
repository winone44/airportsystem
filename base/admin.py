from django.contrib import admin
from .models import Plane, Pilot, Passengers, PlaneFlights, Airport

# Register your models here.


class AirportAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class PlaneFlightsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['from_airport', 'to_airport']


admin.site.register(Plane)
admin.site.register(Pilot)
admin.site.register(Passengers)
admin.site.register(PlaneFlights, PlaneFlightsAdmin)
admin.site.register(Airport, AirportAdmin)

