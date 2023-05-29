import json
import string
import random

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from .models import Flight, Route, Passenger, Bookings
from .forms import SearchForm, BookingForm


def homepage(request):
    return render(request, 'homepage.html', {"form": SearchForm})


def book(request):
    flight_check_box = json.loads(request.POST['check_box'])
    flight_data = Flight.objects.filter(flight_id=flight_check_box['flight_id']).values()
    route_data = Route.objects.filter(route_id=flight_check_box['route_id']).values()
    flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
    route_data = json.dumps(list(route_data), cls=DjangoJSONEncoder)

    context = {
        "form": BookingForm,
        "flight_data": flight_data,
        "route_data": route_data
    }
    request.session['flight'] = flight_check_box[
        'flight_id']
    request.session['route'] = route_data
    return render(request, 'bookings.html', context)


def generate_booking_ref():
    new_ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    while Bookings.objects.filter(booking_id=new_ref).exists():
        new_ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return new_ref


def manage_booking(request):
    flight = request.session['flight']
    flight_instance = Flight.objects.get(flight_id=flight)
    if flight_instance.seats_available > 0:

        passenger = Passenger.objects.create(first_name=request.POST['first_name'],
                                             last_name=request.POST['last_name'],
                                             email=request.POST['email'],
                                             phone_number=request.POST['phone_number'])

        flight_instance.seats_available = flight_instance.seats_available - 1
        flight_instance.save()
        booking = Bookings.objects.create(booking_id=generate_booking_ref(), passenger=passenger,
                                          flight=flight_instance)
        flight_data = vars(flight_instance)
        flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
        passenger = vars(passenger)
        booking = vars(booking)
        passenger.pop('_state')
        passenger['phone_number'] = request.POST['phone_number']
        booking.pop('_state')

        context = {"passenger": passenger,
                   "booking": booking,
                   "flight": flight_data,
                   "route": request.session['route']}
    else:
        context = {"passenger": {'error': 'error'},
                   "booking": {'error': 'error'},
                   "flight": {'error': 'error'},
                   "route": {'error': 'error'}}

    return render(request, 'manageBooking.html', context)


def search(request):
    departure_date = request.POST['departure_date']
    departure_location = request.POST['departure_location']
    arrival_location = request.POST['arrival_location']

    flight_data = Flight.objects.filter(
        date=departure_date,
        route__departure_location=departure_location,
        route__arrival_location=arrival_location, seats_available__gt=0).values()

    route_data = Route.objects.filter(departure_location=departure_location,
                                      arrival_location=arrival_location).values()

    flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
    route_data = json.dumps(list(route_data), cls=DjangoJSONEncoder)

    context = {
        'flight_data': flight_data,
        'route_data': route_data
    }
    return render(request, 'searchFlight.html', context)
