from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

from .views import Account

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
<<<<<<< HEAD:flamingo/accounts/urls.py
    path('account/', views.Account, name='account'),
    path('book/<int:pk>', views.CreateBooking, name='book'),
    path('bookdone/', views.BookDone.as_view(), name='bookdone'),
    path('edit/<int:pk>', views.EditBooking, name='edit'),
    path('delete/<int:pk>', views.DeleteBooking, name='delete'),
    path('car/<int:pk>', views.CarView.as_view(), name='car-details'),
    path('booking/<int:pk>', views.BookingView.as_view(), name='booking-details'),
]
=======
    path('account/', Account.as_view(), name='account'),
]
>>>>>>> master:accounts/urls.py
