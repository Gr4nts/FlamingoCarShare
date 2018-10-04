from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Car
from .models import Booking
#from .models import Available

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email',
                    'license_number', 'country_of_issue', 'state', 'issue_date', 'expiry_date']

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'description', 'price'] #, 'available']
    list_filter = ['price'] #, 'available']

class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car', 'book_start_date', 'book_end_date']
    list_filter = ['customer', 'car']
    date_hierarchy = 'book_start_date'

#class AvailableModelAdmin(admin.ModelAdmin):
    #list_display = ['avail_id', 'available']

admin.site.register(Car,CarModelAdmin)
admin.site.register(Booking,BookingModelAdmin)
#admin.site.register(Available,AvailableModelAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
