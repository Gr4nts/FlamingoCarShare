from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

class HowToUse(TemplateView):
    template_name = 'howtouse.html'

class Prices(TemplateView):
    template_name = 'prices.html'

class About(TemplateView):
    template_name = 'about.html'
