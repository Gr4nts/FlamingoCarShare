from django.contrib import admin
from .models import Car
from .models import Booking

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'description', 'price']
    list_filter = ['price']

class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car', 'book_start_date', 'book_end_date']
    list_filter = ['customer', 'car']
    date_hierarchy = 'book_start_date'

admin.site.register(Car,CarModelAdmin)
admin.site.register(Booking,BookingModelAdmin)
