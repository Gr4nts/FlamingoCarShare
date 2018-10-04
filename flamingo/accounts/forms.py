from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        #fields = '__all__'
        fields = ['book_start_date', 'start_time', 'car']
