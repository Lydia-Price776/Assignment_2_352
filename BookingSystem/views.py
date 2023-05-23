from django.shortcuts import render, redirect

from .forms import SearchForm
from .models import Airport, Flight, Route


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
            departure_flight = Flight.objects.filter(
                date=form.cleaned_data['departure_date']
            )

            context = {'form': form, 'departure_flight': departure_flight}

            # Render the template with the form and retrieved data
            return render(request, 'searchFlight.html', context)
    else:
        form = SearchForm()

    return render(request, 'searchFlight.html', {'form': form})
