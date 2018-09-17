from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['car_id', 'book_start_date', 'book_end_date']
