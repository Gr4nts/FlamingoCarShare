from django.urls import path

from . import views

from .views import Account

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', Account.as_view(), name='account'),
]