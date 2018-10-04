from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from .models import Car
from .models import Booking
from .forms import BookingForm
#from django.views.generic import DetailView

class SignUp(SuccessMessageMixin,generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    success_message = "You have successfully signed up!"

def Account(request):
    Bookings = Booking.objects.filter(customer=request.user).order_by('-book_start_date')
    context = { 'Bookings': Bookings }
    return render(request, 'account.html', context)

def CreateBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            bform = form.save(commit=False)
            bform.customer = request.user
            bform.save()
            #form.save()
            messages.success(request, 'Your booking has been saved!')
            return redirect('account')
    else:
        form = BookingForm(request.POST)
    #return render(request, 'book.html', {'form': form})
    return render(request, 'map.html', {'bform': bform})

class CarView(generic.DetailView):
    template_name = 'car_details.html'
    model = Car

class BookingView(generic.DetailView):
    template_name = 'booking_details.html'
    model = Booking
