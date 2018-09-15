from django.db import models
#from django.conf import settings
#from django.utils import timezone
#import datetime
from django.contrib.auth.models import User


class Car(models.Model):
    car_id = models.IntegerField("Car", primary_key=True)
    car_name = models.CharField("Car", max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='car_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField("Availablility", default=True)
    lat = models.CharField(max_length=50, null=True, blank=True)
    lng = models.CharField(max_length=50, null=True, blank=True)
    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})
    def __str__(self):
        return self.car_name

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    #customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='my_books')
    customer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Customer")
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Car")
    book_start_date = models.DateTimeField("Start date", null=True, blank=True)
    book_end_date = models.DateTimeField("End date", null=True, blank=True)
    #is_available = models.ForeignKey(Car, on_delete=models.CASCADE,default=False)
    def get_absolute_url(self):
        return reverse('booking-details', kwargs={'pk': self.pk})
    def __str__(self):
        return str(self.customer)
