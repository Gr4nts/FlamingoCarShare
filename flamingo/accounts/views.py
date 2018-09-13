from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .models import Booking
from django.http import HttpResponseRedirect
#from .forms import CreateBookForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def Account(request):
    Bookings = Booking.objects.filter(customer=request.user)
    context = { 'Bookings': Bookings }
    return render(request, 'account.html', context)

class CreateBook(generic.CreateView):
    template_name = 'book.html'
    
    model = Booking
"""
def CreateBook(request):
"""