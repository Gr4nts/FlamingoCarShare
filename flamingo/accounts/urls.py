from django.urls import path
from . import views
from .views import Account

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', views.Account, name='account'),
    path('book/', views.CreateBook.as_view(), name='book'),

]
