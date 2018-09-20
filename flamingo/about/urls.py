from django.urls import path
from . import views

urlpatterns = [
    path('howtouse/', views.HowToUse.as_view(), name='howtouse'),
    path('prices/', views.Prices.as_view(), name='prices'),
    path('about/', views.About.as_view(), name='about'),
    #homepage
    path('', views.Home, name='home'),
]
