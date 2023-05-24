import json

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from .forms import SearchForm
from .models import Flight, Route


def homepage(request):
    return render(request, 'homepage.html', {})


def book(request):
    return render(request, 'bookings.html', {})


def manage_booking(request):
    return render(request, 'manageBooking.html', {})


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            departure_location = form.cleaned_data['departure_location']
            arrival_location = form.cleaned_data['arrival_location']
            flight_data = Flight.objects.filter(
                date=form.cleaned_data['departure_date'],
                route__departure_location=departure_location,
                route__arrival_location=arrival_location).values()

            route_data = Route.objects.filter(departure_location=departure_location,
                                              arrival_location=arrival_location).values()

            flight_data = json.dumps(list(flight_data), cls=DjangoJSONEncoder)
            route_data = json.dumps(list(route_data), cls=DjangoJSONEncoder)
            context = {'form': form, 'flight_data': flight_data, 'route_data': route_data}
            return render(request, 'searchFlight.html', context)

    else:
        form = SearchForm()

    return render(request, 'searchFlight.html', {'form': form})
