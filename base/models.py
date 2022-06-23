from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class Plane(models.Model):
    name = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    number_of_seats = models.IntegerField()
    is_economy_class = models.BooleanField()
    is_business_class = models.BooleanField()
    is_first_class = models.BooleanField()

    def __str__(self):
        return str(self.id) + '. ' + self.producer + ' ' + self.name


class Pilot(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    house_number = models.CharField(max_length=20)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    numberID = models.CharField(max_length=20)
    passport_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ' ' + self.first_name + ' ' + self.last_name


class Airport(models.Model):
    id = models.IntegerField(primary_key=True)
    ident = models.TextField()
    type = models.TextField()
    name = models.TextField()
    latitude_deg = models.DecimalField(max_digits=20, decimal_places=17)
    longitude_deg = models.DecimalField(max_digits=20, decimal_places=17)
    elevation_ft = models.IntegerField()
    continent = models.TextField()
    iso_country = models.TextField()
    iso_region = models.TextField()
    municipality = models.TextField()
    scheduled_service = models.TextField()
    gps_code = models.TextField()
    iata_code = models.TextField()
    local_code = models.TextField()
    home_link = models.URLField()
    wikipedia_link = models.URLField()
    keywords = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.iata_code


class PlaneFlights(models.Model):

    class statusType(models.IntegerChoices):
        CANCELLED = 0, _('Cancelled')
        SCHEDULED = 1, _('Scheduled')
        SCHEDULED_DELAYED = 2, _('Scheduled Delayed')
        GO_TO_YOUR_GATE = 3, _('Go to your gate')
        LAST_CALL = 4, _('Last call')
        EN_ROUTE = 5, _('En Route')
        EN_ROUTE_DELAYED = 6, _('En Route Delayed')
        LANDED = 7, _('Landed')
        LANDED_DELAYED = 8, _('Landed Delayed')

    flight = models.CharField(max_length=200, unique=True)
    carrier = models.CharField(max_length=200)
    from_airport = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name="from_airport_FK")
    to_airport = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name="to_airport_FK")
    plane = models.ForeignKey(Plane, on_delete=models.SET_NULL, null=True)
    pilot = models.ForeignKey(Pilot, on_delete=models.SET_NULL, null=True)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    terminal = models.CharField(max_length=2, default='A')
    gate = models.CharField(max_length=2, default='1')
    status = models.IntegerField(choices=statusType.choices)
    is_delay = models.BooleanField(default=False)
    delay_time_in_h = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.departure_datetime) + ' form ' + self.from_airport.name + ' to ' + self.to_airport.name


class Passengers(models.Model):

    class sexType(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    flight = models.ForeignKey(PlaneFlights, on_delete=models.SET_NULL, null=True)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    house_number = models.CharField(max_length=20)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    numberID = models.CharField(max_length=20, null=True, blank=True)
    passport_number = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=sexType.choices)
    reserved_seat = models.CharField(max_length=200)
    is_extra_baggage = models.BooleanField()
    baggage_number = models.CharField(max_length=30, null=True, blank=True, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.date_of_birth)
