from django import forms
from phonenumber_field.formfields import PhoneNumberField

Airports = [
    ('NZNE', 'Dairy Flat, New Zealand (NZNE)'),
    ('YMHB', 'Hobart, Australia (YMHB)'),
    ('NZRO', 'Rotorua, New Zealand (NZRO)'),
    ('NZGB', 'Great Barrier Island, New Zealand(NZGB)'),
    ('NZCI', 'Tuuta, Chatham Islands (NZCI)'),
    ('NZLT', 'Lake Tekapo, New Zealand (NZLT)'),
]


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchFlightForm(forms.Form):
    departure_date = forms.DateField(widget=DateInput)
    departure_location = forms.CharField(label='From',
                                         widget=forms.Select(choices=Airports))
    arrival_location = forms.CharField(label='To',
                                       widget=forms.Select(choices=Airports))


class SearchBookingForm(forms.Form):
    booking_ref = forms.CharField(label='Booking Reference')


class BookingForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    phone_number = PhoneNumberField(label='Phone Number', required=False)
    phone_number.error_messages['invalid'] = 'Please enter a valid phone number including country code'
