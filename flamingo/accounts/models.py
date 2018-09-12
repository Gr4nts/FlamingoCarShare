from django.db import models
from django.conf import settings

class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_name = models.CharField(max_length=50)
        #image = models.ImageField(upload_to='car_images')
        #image = models.ImageField(upload_to='{% static 'img/car_images' %}')
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})
    def __str__(self):
        return self.car_name

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    book_start_date = models.DateTimeField()
    book_end_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    Car.is_available = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('booking-details', kwargs={'pk': self.pk})
    def __str__(self):
        return str(self.customer)
