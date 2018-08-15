from django.urls import path

from . import views

from .views import Map

urlpatterns = [
    path('map/', Map.as_view(), name='map'),
]