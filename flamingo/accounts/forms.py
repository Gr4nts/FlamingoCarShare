from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
<<<<<<< HEAD
        fields = ['car', 'book_start_date', 'book_end_date']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
            model = CustomUser
            fields = ['username', 'first_name', 'last_name', 'email', 'license_number',
                      'country_of_issue', 'state', 'issue_date', 'expiry_date', ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'license_number',
                  'country_of_issue', 'state', 'issue_date', 'expiry_date', ]
=======
        #fields = '__all__'
        fields = ['book_start_date', 'start_time', 'car']
>>>>>>> d-grace
