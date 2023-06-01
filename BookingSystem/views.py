import datetime
import json
import string
import random

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from .models import Flight, Route, Passenger, Bookings, Airport
from .forms import SearchFlightForm, BookingForm, SearchBookingForm


def homepage(request):
    context = {
        "form_flight": SearchFlightForm,
        "form_booking": SearchBookingForm
    }
    return render(request, 'homepage.html', context)


def book(request):
    flight_check_box = json.loads(request.POST['check_box'])
    flight_data = Flight.objects.filter(flight_id=flight_check_box['flight_id']).values()
    route_data = Route.objects.filter(route_id=flight_check_box['route_id']).values()
    airport_departure = Airport.objects.filter(code=route_data[0]['departure_location_id']).values()[0]['name']
    airport_arrival = Airport.objects.filter(code=route_data[0]['arrival_location_id']).values()[0]['name']
    flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
    route_data = json.dumps(list(route_data), cls=DjangoJSONEncoder)

    context = {
        "form": BookingForm,
        "flight_data": flight_data,
        "route_data": route_data,
        'airports': {'departure': airport_departure, 'arrival': airport_arrival}

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


def view_booking(request):
    context = {"passenger": {'error': 'error'},
               "booking": {'error': 'unable to retrieve booking'},
               "flight": {'error': 'error'},
               "route": {'error': 'error'}}
    if 'booking_ref' in request.POST:

        if Bookings.objects.filter(booking_id=request.POST['booking_ref']).exists():
            booking = vars(Bookings.objects.get(booking_id=request.POST['booking_ref']))
            context = get_booking(request, booking)
    else:

        flight_id = request.session['flight']
        if Bookings.objects.filter(passenger_id__first_name=request.POST['first_name'],
                                   passenger_id__last_name=request.POST['last_name'],
                                   flight_id=flight_id).exists():
            passengers = Passenger.objects.filter(first_name=request.POST['first_name'],
                                                  last_name=request.POST['last_name'])
            flight = Flight.objects.get(flight_id=flight_id)

            for passenger in passengers:

                if Bookings.objects.filter(passenger_id=passenger, flight_id=flight).exists():
                    booking = vars(Bookings.objects.get(passenger_id=passenger, flight_id=flight))
                    context = get_booking(request, booking)
        else:
            context = {"passenger": {'error': 'error'},
                       "booking": {'error': 'unable to make booking'},
                       "flight": {'error': 'error'},
                       "route": {'error': 'error'}}
            flight_instance = Flight.objects.get(flight_id=flight_id)
            if flight_instance.seats_available > 0:
                context = make_booking(flight_id, flight_instance, request)

    return render(request, 'viewBooking.html', context)


def make_booking(flight, flight_instance, request):
    passenger = Passenger.objects.create(first_name=request.POST['first_name'],
                                         last_name=request.POST['last_name'],
                                         email=request.POST['email'],
                                         phone_number=request.POST['phone_number'])
    flight_instance.seats_available = flight_instance.seats_available - 1
    flight_instance.save()
    booking = vars(Bookings.objects.create(booking_id=generate_booking_ref(), passenger=passenger,
                                           flight=flight_instance))
    flight_data = Flight.objects.filter(flight_id=flight).values()
    flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
    passenger = vars(passenger)
    passenger.pop('_state')
    passenger['phone_number'] = '+' + str(passenger['phone_number'].country_code) + \
                                str(passenger['phone_number'].national_number)
    booking.pop('_state')
    context = {"passenger": passenger,
               "booking": booking,
               "flight": flight_data,
               "route": request.session['route']}
    return context


def get_booking(request, booking):
    passenger = vars(Passenger.objects.get(passenger_id=booking['passenger_id']))
    flight = Flight.objects.filter(flight_id=booking['flight_id']).values()
    route = Route.objects.filter(route_id=flight[0]['route_id']).values()
    passenger['phone_number'] = '+' + str(passenger['phone_number'].country_code) + \
                                str(passenger['phone_number'].national_number)
    flight = json.dumps(list(flight), cls=DjangoJSONEncoder)
    route = json.dumps(list(route), cls=DjangoJSONEncoder)
    booking.pop('_state')
    passenger.pop('_state')
    return {"passenger": passenger,
            "booking": booking,
            "flight": flight,
            "route": route}


def search(request):
    departure_date = request.POST['departure_date']
    departure_location = request.POST['departure_location']
    arrival_location = request.POST['arrival_location']
    current_date = datetime.datetime.now()
    if datetime.datetime.strptime(departure_date, '%Y-%m-%d') < current_date:
        context = {'flight_data': {'error': 'error'},
                   'route_data': {'error': 'error'},
                   'airports': {'error': 'error'}}
    else:
        context = display_flight_matches(arrival_location,
                                         departure_date, departure_location)
    return render(request, 'searchFlight.html', context)


def display_flight_matches(arrival_location, departure_date, departure_location):
    flight_data = Flight.objects.filter(
        date=departure_date,
        route__departure_location=departure_location,
        route__arrival_location=arrival_location, seats_available__gt=0).values()
    route_data = Route.objects.filter(departure_location=departure_location,
                                      arrival_location=arrival_location).values()
    airport_departure = Airport.objects.filter(code=departure_location).values()[0]['name']
    airport_arrival = Airport.objects.filter(code=arrival_location).values()[0]['name']
    flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
    route_data = json.dumps(list(route_data), cls=DjangoJSONEncoder)
    context = {
        'flight_data': flight_data,
        'route_data': route_data,
        'airports': {'departure': airport_departure, 'arrival': airport_arrival}
    }
    return context


def cancel_booking(request):
    print(request.POST)
    booking_to_cancel = request.POST.get('cancel_data')
    to_delete = Bookings.objects.filter(booking_id=booking_to_cancel)
    print(to_delete)

    if to_delete.exists():
        departure_date = Flight.objects.filter(flight_id=to_delete.values()[0]['flight_id']).values()[0]['date']
        print(departure_date)
        current_date = datetime.date.today()
        if departure_date < current_date:
            context = {'outcome': 'date error'}
        else:
            to_delete.delete()
            context = {'outcome': 'success'}
    else:
        context = {'outcome': 'error'}

    return render(request, 'cancelBooking.html', context)
