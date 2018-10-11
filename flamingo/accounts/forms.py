from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        #fields = '__all__'
        fields = ['car', 'book_start_date', 'book_end_date', 'start_time', 'end_time']
        #widgets = { 'book_start_date': DateInput(), 'start_time': TimeInput() }
        #widgets = { 'name': TextInput(attrs={'placeholder': 'name'}), }

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
