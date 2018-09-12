from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .models import Booking

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def Account(request):
    Bookings = Booking.objects.all()
    context = { 'Bookings': Bookings }
    return render(request, 'account.html', context)









#class CreateBook(generic.CreateView):
    #booking = Booking
    #template_name = 'book.html'

def CreateBook(request):
    #if request.method == 'POST':
        #if request.POST.get('car_id') and request.POST.get('book_start_date') and request.POST.get('book_end_time'):
            #Bookings=Booking()
            #Bookings.car_id= request.POST.get('car_id')
            #Bookings.book_start_date= request.POST.get('book_start_date')
            #Bookings.book_end_time= request.POST.get('book_end_time')
            #Bookings.save()
            #return render(request, 'book.html')  
    #else:
        #return render(request,'book.html')
        
    booking = Booking.objects.all()
    form = request.POST
    if request.method == 'POST':
        selected_car = get_object_or_404(booking, pk=request.POST.get('car_id'))
        booking.car_id = selected_car
        booking.save()
    #return render_to_response ('book.html', {'cars':car}, context_instance = RequestContext(request),)
    return render(request, 'book.html')
