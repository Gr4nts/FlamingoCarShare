from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from accounts.models import Car

class Prices(TemplateView):
    template_name = 'prices.html'

class About(TemplateView):
    template_name = 'about.html'

def Home(request):
    Cars = Car.objects.all()
    Cars1 = Car.objects.filter(icon=1)
    Cars2 = Car.objects.filter(icon=2)
    Cars3 = Car.objects.filter(icon=3)
    context = { 'Cars': Cars, 'Cars1': Cars1, 'Cars2': Cars2, 'Cars3': Cars3 }
    return render(request, 'home.html', context)
