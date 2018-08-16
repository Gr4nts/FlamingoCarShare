from django.shortcuts import render

from django.views.generic import TemplateView

class Map(TemplateView):
    template_name = 'map.html'
    
