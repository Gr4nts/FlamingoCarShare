from django.urls import path
from . import views
from .views import About

urlpatterns = [
    path('howtouse/', views.HowToUse.as_view(), name='howtouse'),
    path('prices/', views.Prices.as_view(), name='prices'),
    path('about/', views.About.as_view(), name='about'),
]