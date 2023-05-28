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
    flight_data = json.loads(request.POST['check_box'])
    print(flight_data)
    route_data = Route.objects.filter(route_id=flight_data["route_id"]).values()
    route_data = json.dumps(list(route_data), cls=DjangoJSONEncoder)
    context = {
        "form": BookingForm,
        "flight_data": flight_data,
        "route_data": route_data
    }
    request.session['flight'] = flight_data
    request.session['route'] = route_data
    return render(request, 'bookings.html', context)


def generate_booking_ref():
    new_ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    while Bookings.objects.filter(booking_id=new_ref).exists():
        new_ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return new_ref


def manage_booking(request):
    # if request.method == 'POST':

    passenger = Passenger.objects.create(first_name=request.POST['first_name'],
                                         last_name=request.POST['last_name'],
                                         email=request.POST['email'],
                                         phone_number=request.POST['phone_number'])

    flight = request.session['flight']
    flight_instance = Flight.objects.get(flight_id=flight["flight_id"])
    booking = Bookings.objects.create(booking_id=generate_booking_ref(), passenger=passenger, flight=flight_instance)
    passenger = vars(passenger)
    booking = vars(booking)
    passenger.pop('_state')
    booking.pop('_state')
    context = {"passenger": passenger,
               "booking": booking,
               "flight": flight,
               "route": request.session['route']}

    return render(request, 'manageBooking.html', context)


def search(request):
    departure_date = request.POST['departure_date']
    departure_location = request.POST['departure_location']
    arrival_location = request.POST['arrival_location']

    flight_data = Flight.objects.filter(
        date=departure_date,
        route__departure_location=departure_location,
        route__arrival_location=arrival_location).values()

    route_data = Route.objects.filter(departure_location=departure_location,
                                      arrival_location=arrival_location).values()

    flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
    route_data = json.dumps(list(route_data), cls=DjangoJSONEncoder)

    context = {
        'flight_data': flight_data,
        'route_data': route_data
    }
    return render(request, 'searchFlight.html', context)
