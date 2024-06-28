"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from blog.views import pricefilter,contact,home
# from blog.views import contact_view

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('Pricefilter/', pricefilter, name='pricefilter'),
    path('contact/',contact,name='contact_view'),
    path('',home,name='home')
    # path('property_map/',property_map_view,name='property_map')
]



