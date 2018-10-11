from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #Add additional fields here
    first_name = models.CharField("First Name", max_length=50, null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=50, null=True, blank=True)
    email = models.CharField("Email", max_length=50, null=True, blank=True)
    license_number = models.IntegerField("License Number", null=True, blank=True)
    country_of_issue = models.CharField("Country Of Issue", max_length=50, null=True, blank=True)
    state = models.CharField("State", max_length=50, null=True, blank=True)
    issue_date = models.DateField("Issue Date", null=True, blank=True)
    expiry_date = models.DateField("Expiry Date", null=True, blank=True)

    def __str__(self):
        #return self.email
        return  str(self.first_name + " " + self.last_name)

class Car(models.Model):
    car_id = models.IntegerField("Car", primary_key=True)
    car_name = models.CharField("Model", max_length=50, null=True, blank=True)
    image = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField("Price per day", null=True, blank=True)
    lat = models.CharField(max_length=50, null=True, blank=True)
    lng = models.CharField(max_length=50, null=True, blank=True)
    icon = models.IntegerField("Car Image Icon", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})
    def __str__(self):
        return self.car_name

class Booking(models.Model):
    booking_id = models.AutoField("Booking", primary_key=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Customer")
    book_start_date = models.DateField("Start date", null=True, blank=True)
    book_end_date = models.DateField("End date", null=True, blank=True)
    start_time = models.TimeField("Start time", null=True, blank=True)
    end_time = models.TimeField("End time", null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Cars")
    status = models.CharField("Status", max_length=20, null=True, blank=True, default="Pending")
    status_button = models.CharField(max_length=20, null=True, blank=True, default="primary")
    status_options = models.TextField(null=True, blank=True, default="Status(button): Pending (primary), Paid(success), Cancelled(danger)")

    def get_absolute_url(self):
        return reverse('booking-details', kwargs={'pk': self.pk})
    def __str__(self):
        return str(self.customer)
