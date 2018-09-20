from django.contrib import admin
from .models import Car
from .models import Booking
#from .models import Available

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
