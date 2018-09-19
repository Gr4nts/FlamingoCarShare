from django.contrib import admin
from .models import Car
from .models import Booking

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'description', 'price', 'is_available']
    list_filter = ['price', 'is_available']

class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car_id', 'book_start_date', 'book_end_date', 'car_available']
    list_filter = ['customer', 'car_id']
    date_hierarchy = 'book_start_date'

    def car_available(self, Booking):
        return Booking.car_id.is_available
        car_available.admin_order_field = 'car_id'


admin.site.register(Car,CarModelAdmin)
admin.site.register(Booking,BookingModelAdmin)
