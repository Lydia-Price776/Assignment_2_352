import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Assignment2.settings")

import django

django.setup()

from BookingSystem.models import Plane, Airport, Route, Flight, Bookings, Passenger
import datetime

planes = [
    (6, 'SyberJet SJ30i'),
    (4, 'Cirrus SF50'),
    (4, 'Cirrus SF50'),
    (5, 'HondaJet Elite'),
    (5, 'HondaJet Elite')
]

for seats, plane_type in planes:
    Plane(seats=seats, type=plane_type).save()

airports = [
    ('NZNE', 'Dairy Flat', 'UTC+12'),
    ('YMHB', 'Hobart', 'UTC+10'),
    ('NZRO', 'Rotorua', 'UTC+12'),
    ('NZCI', 'Tuuta', 'UTC+12:45'),
    ('NZGB', 'Claris', 'UTC+12'),
    ('NZLT', 'Lake Tekapo', 'UTC+12'),
]

for code, name, time_zone in airports:
    Airport(code=code, name=name, time_zone=time_zone).save()

routes = [
    ('DFHO06', datetime.time(6, 0), datetime.time(8, 40), 40, Airport.objects.get(code='NZNE'),
     Airport.objects.get(code='YMHB'), Airport.objects.get(code='NZRO')),
    ('HODF14', datetime.time(14, 0), datetime.time(19, 0), None, Airport.objects.get(code='YMHB'),
     Airport.objects.get(code='NZNE'), None),
    ('DFRO06', datetime.time(6, 0), datetime.time(6, 45), None, Airport.objects.get(code='NZNE'),
     Airport.objects.get(code='NZRO'), None),
    ('RODF12', datetime.time(12, 0), datetime.time(12, 45), None, Airport.objects.get(code='NZRO'),
     Airport.objects.get(code='NZNE'), None),
    ('DFRO16', datetime.time(16, 0), datetime.time(16, 45), None, Airport.objects.get(code='NZNE'),
     Airport.objects.get(code='NZRO'), None),
    ('RODF19', datetime.time(19, 0), datetime.time(19, 45), None, Airport.objects.get(code='NZRO'),
     Airport.objects.get(code='NZNE'), None),
    ('DFGB09', datetime.time(9, 0), datetime.time(9, 40), None, Airport.objects.get(code='NZNE'),
     Airport.objects.get(code='NZGB'), None),
    ('GBDF09', datetime.time(9, 0), datetime.time(9, 40), None, Airport.objects.get(code='NZGB'),
     Airport.objects.get(code='NZNE'), None),
    ('DFCI10', datetime.time(9, 0), datetime.time(13, 0), None, Airport.objects.get(code='NZNE'),
     Airport.objects.get(code='NZCI'), None),
    ('CIDF10', datetime.time(9, 0), datetime.time(12, 30), None, Airport.objects.get(code='NZCI'),
     Airport.objects.get(code='NZNE'), None),
    ('DFLT13', datetime.time(13, 0), datetime.time(14, 15), None, Airport.objects.get(code='NZNE'),
     Airport.objects.get(code='NZLT'), None),
    ('LTDF13', datetime.time(13, 0), datetime.time(14, 15), None, Airport.objects.get(code='NZLT'),
     Airport.objects.get(code='NZNE'), None),
]

for ID, depatureTime, arrivalTime, stopOverTime, depatureLocation, arrivalLocation, stopoverLocation in routes:
    Route.objects.create(route_id=ID, departure_time=depatureTime, arrival_time=arrivalTime, stopover_time=stopOverTime,
                         departure_location=depatureLocation, arrival_location=arrivalLocation,
                         stopover_location=stopoverLocation)


def daily_flight(plane_id, route_id, date, price, seats):
    days = 1
    for x in range(365):
        Flight(plane=plane_id, route=route_id, date=date, price=price, seats_available=seats).save()
        days += 1
        if days <= 5:
            date = date + datetime.timedelta(1)
        else:
            date = date + datetime.timedelta(3)
            days = 1


def twice_weekly_flight(plane_id, route_id, date, price, seats):
    days = 2
    for x in range(112):
        Flight(plane=plane_id, route=route_id, date=date, price=price, seats_available=seats).save()
        days += 3
        if days <= 5:
            date = date + datetime.timedelta(3)
        else:
            date = date + datetime.timedelta(4)
            days = 2


def three_weekly_flight(plane_id, route_id, date, price, seats):
    days = 1
    for x in range(55):
        Flight(plane=plane_id, route=route_id, date=date, price=price, seats_available=seats).save()
        days += 2
        if days <= 5:
            date = date + datetime.timedelta(2)
        else:
            date = date + datetime.timedelta(3)
            days = 1


def weekly_flight(plane_id, route_id, date, price, seats):
    for x in range(55):
        Flight(plane=plane_id, route=route_id, date=date, price=price, seats_available=seats).save()
        date = date + datetime.timedelta(7)


# DAIRY FLAT TO HOBART
weekly_flight(Plane.objects.get(plane_id=1), Route.objects.get(route_id='DFHO06'), datetime.date(2023, 5, 26), 449.99,
              6)

# HOBART TO DAIRY FLAT
weekly_flight(Plane.objects.get(plane_id=1), Route.objects.get(route_id='HODF14'), datetime.date(2023, 5, 28), 449.99,
              6)

# DAIRY FLAT TO ROTORUA 0600
daily_flight(Plane.objects.get(plane_id=2), Route.objects.get(route_id='DFRO06'), datetime.date(2023, 5, 22), 69.99, 4)

# ROTORUA TO DAIRY FLAT 1200
daily_flight(Plane.objects.get(plane_id=2), Route.objects.get(route_id='RODF12'), datetime.date(2023, 5, 22), 69.99, 4)

# DAIRY FLAT TO ROTORUA 1600
daily_flight(Plane.objects.get(plane_id=2), Route.objects.get(route_id='DFRO16'), datetime.date(2023, 5, 22), 69.99, 4)

# ROTORUA TO DAIRY FLAT 1900
daily_flight(Plane.objects.get(plane_id=2), Route.objects.get(route_id='RODF19'), datetime.date(2023, 5, 22), 69.99, 4)

# DAIRY FLAT TO GREAT BARRIER
three_weekly_flight(Plane.objects.get(plane_id=3), Route.objects.get(route_id='DFGB09'), datetime.date(2023, 5, 22),
                    129.49, 4)

# GREAT BARRIER TO DAIRY FLAT
three_weekly_flight(Plane.objects.get(plane_id=3), Route.objects.get(route_id='GBDF09'), datetime.date(2023, 5, 23),
                    129.49, 4)

# DAIRY FLAT TO CHATHAMS
twice_weekly_flight(Plane.objects.get(plane_id=4), Route.objects.get(route_id='DFCI10'), datetime.date(2023, 5, 23),
                    334.99, 5)

# CHATHAMS TO DAIRY FLAT
twice_weekly_flight(Plane.objects.get(plane_id=4), Route.objects.get(route_id='CIDF10'), datetime.date(2023, 5, 24),
                    334.99, 5)

#  DAIRY FLAT TO LAKE TEKAPO
weekly_flight(Plane.objects.get(plane_id=5), Route.objects.get(route_id='DFLT13'), datetime.date(2023, 5, 22), 95.49, 5)

# LAKE TEKAPO TO  DAIRY FLAT
weekly_flight(Plane.objects.get(plane_id=5), Route.objects.get(route_id='LTDF13'), datetime.date(2023, 5, 23), 95.49, 5)
