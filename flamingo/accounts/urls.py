from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', views.Account, name='account'),
    path('book/', views.CreateBooking, name='book'),

    #path(r'^car/(?P<pk>\d+)/$', views.CarView.as_view(), name='car-details'),
    #path(r'^booking/(?P<pk>\d+)/$', views.BookingView.as_view(), name='booking-details'),

    path('car/<int:pk>', views.CarView.as_view(), name='car-details'),
    path('booking/<int:pk>', views.BookingView.as_view(), name='booking-details'),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
