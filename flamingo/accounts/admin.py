from django.contrib import admin

from .models import Car
from .models import Booking

#class BookingModelAdmin(admin.ModelAdmin):
    #list_display = ['user_id', 'user_first_name', 'user_last_name', 'user_email']
    #search_fields = ['Booking.customer']

admin.site.register(Car)
admin.site.register(Booking)
#admin.site.register(Booking,BookingModelAdmin)