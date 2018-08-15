"""flamingo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.views.generic.base import TemplateView
#added
from django.conf.urls.static import static
#added
#from django.conf import settings

#load order - top to bottom
urlpatterns = [
    # path(url address, path to view, url name) #

    #home view
      path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #authenticate
      path('admin/', admin.site.urls),
    
    #signup
      path('', include('accounts.urls')),
    #login
      path('', include('django.contrib.auth.urls')),
    #map
      path('', include('map.urls')),
]

#dev test
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




