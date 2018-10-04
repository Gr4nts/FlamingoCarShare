from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

class SignUp(generic.CreateView):
    form_class = UserCreationForm #form
    success_url = reverse_lazy('login') #page when successful
    template_name = 'signup.html' #html page
    
class Account(TemplateView):
    template_name = 'account.html'