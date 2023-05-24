from django.db import models


# Create your models here.

class Plane(models.Model):
    plane_id = models.AutoField(primary_key=True)
    seats = models.IntegerField()
    type = models.CharField(max_length=50)

    class Meta:
        db_table = 'Plane'


class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True)
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Passenger'


class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, primary_key=True)
    time_zone = models.CharField(max_length=50)

    class Meta:
        db_table = 'Airport'


class Route(models.Model):
    route_id = models.CharField(max_length=100, primary_key=True)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    stopover_time = models.IntegerField(blank=True, null=True)
    departure_location = models.ForeignKey(Airport, related_name='depature_location',
                                           on_delete=models.CASCADE)
    arrival_location = models.ForeignKey(Airport, related_name='arrival_location',
                                         on_delete=models.CASCADE)
    stopover_location = models.ForeignKey(Airport, related_name='stopover_location',
                                          on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'Route'


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    plane = models.ForeignKey(Plane, related_name='plane', on_delete=models.CASCADE)
    route = models.ForeignKey(Route, related_name='route', on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()

    class Meta:
        db_table = 'Flight'


class Bookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    passenger = models.ForeignKey(Passenger, related_name='passenger', on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, related_name='flight', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Bookings'
