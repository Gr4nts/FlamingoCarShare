from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from .models import Car
from .models import Booking
from .forms import BookingForm
from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUp(generic.CreateView,SuccessMessageMixin):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    success_message = "You have successfully signed up!"

def Account(request):
    Bookings = Booking.objects.filter(customer=request.user).order_by('-book_start_date')
    context = { 'Bookings': Bookings }
    return render(request, 'account.html', context)

def CreateBooking(request, pk):
#def CreateBooking(request):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            bform = form.save(commit=False)
            bform.customer = request.user
            bform.save()
            messages.success(request, 'Your booking has been saved!')
            return redirect('bookdone')
    else:
        form = BookingForm(request.POST)
    return render(request, 'book.html', {'form': form, 'car' : car})

class BookDone(generic.TemplateView):
    template_name = 'bookdone.html'

class DeleteBooking(generic.DeleteView,SuccessMessageMixin):
    model = Booking
    template_name = 'deletebook.html'
    success_url = reverse_lazy('account')
    success_message = "Booking has been deleted."
    #Bookings = Booking.objects.filter(customer=request.user)

    """def get_queryset(self):
        return Booking.objects.filter(customer=request.user)"""

    """def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       if self.object.customer == request.user:
          self.object.delete()
          return redirect('bookdone')
      else:
          raise Http404"""

    """def delete(self, request, *args, **kwargs):
        if self.object.customer = request.user:
            self.object.delete()
        #success_url = self.get_success_url()
        self.object.delete()
        return redirect('bookdone')"""

class CarView(generic.DetailView):
    model = Car
    template_name = 'car_details.html'

class BookingView(generic.DetailView):
    model = Booking
    template_name = 'booking_details.html'
