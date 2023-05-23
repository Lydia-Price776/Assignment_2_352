from django import forms

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


class SearchForm(forms.Form):
    departure_date = forms.DateField(widget=DateInput)
    return_date = forms.DateField(widget=DateInput)

    departure_location = forms.CharField(label='From',
                                         widget=forms.Select(choices=Airports))
    arrival_location = forms.CharField(label='To',
                                       widget=forms.Select(choices=Airports))
