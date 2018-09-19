from django import forms
from django.forms import ModelForm
from .models import Booking
#from bootstrap_datepicker_plus import DatePickerInput

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['car_id', 'book_start_date', 'book_end_date']
        def queryset(self, request):
            return super(BookingForm, self).queryset(request).select_related('car_id')
