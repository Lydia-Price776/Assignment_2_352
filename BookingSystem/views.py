import json
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from .models import Flight, Route
from .forms import SearchForm


def homepage(request):
    return render(request, 'homepage.html', {"form": SearchForm})


def book(request):
    print(request.POST)
    return render(request, 'bookings.html', {})


def manage_booking(request):
    return render(request, 'manageBooking.html', {})


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
