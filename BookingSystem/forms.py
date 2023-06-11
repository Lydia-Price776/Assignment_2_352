from django import forms
from phonenumber_field.formfields import PhoneNumberField

# Airport information to add to select widget
# This would have been preferable to get the airports from the database and load it that way
Airports = [
    ('NZNE', 'Dairy Flat, New Zealand (NZNE)'),
    ('YMHB', 'Hobart, Australia (YMHB)'),
    ('NZRO', 'Rotorua, New Zealand (NZRO)'),
    ('NZGB', 'Great Barrier Island, New Zealand(NZGB)'),
    ('NZCI', 'Tuuta, Chatham Islands (NZCI)'),
    ('NZLT', 'Lake Tekapo, New Zealand (NZLT)'),
]


# Date input to be used in other forms
class DateInput(forms.DateInput):
    input_type = 'date'


# Form to search for flights by date, departure and arrival locations
class SearchFlightForm(forms.Form):
    departure_date = forms.DateField(widget=DateInput)
    departure_location = forms.CharField(label='From',
                                         widget=forms.Select(choices=Airports))
    arrival_location = forms.CharField(label='To',
                                       widget=forms.Select(choices=Airports))


# Form to search for a booking by reference
class SearchBookingForm(forms.Form):
    booking_ref = forms.CharField(label='Booking Reference')


# Form to create booking
class BookingForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    phone_number = PhoneNumberField(label='Phone Number', required=False)
    phone_number.error_messages['invalid'] = \
        'Please enter a valid phone number including country code. For Example: +64 0274 571 326'
