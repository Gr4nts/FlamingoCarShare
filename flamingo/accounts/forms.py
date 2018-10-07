from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        #fields = '__all__'
        fields = ['car', 'book_start_date', 'start_time']

        #def __init__(self, data=None, files=None, request=None, recipient_list=None, *args, **kwargs):
            #super().__init__(data=data, files=files, request=request, recipient_list=recipient_list, *args, **kwargs)
        """
        def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
            self.fields['id_book_start_date'].widget.attrs['type'] = 'date'
            self.fields['id_start_time'].widget.attrs['type'] = 'time'
        """

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
