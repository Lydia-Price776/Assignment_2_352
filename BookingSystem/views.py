from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {})


def book(request):
    return render(request, 'bookings.html', {})


def manage_booking(request):
    return render(request, 'manageBooking.html', {})


def search(request):
    return render(request, 'searchFlight.html', {})
