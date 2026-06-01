"""
URL configuration for hospitalappointment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from doctorsprofile import views as d_v
from patientsaccount import views as  pa_v
from patients import views as p_v
from appointmentbooking import views as ab_v
from appointmenthistory import views as ah_v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',d_v.up),
    path('book/',d_v.bookings),
    path('test/',pa_v.push),
    path('put/',p_v.get),
    path('',ab_v.home),
    path('login/',ab_v.login),
    path('register/',ab_v.register),
    path('history/',ah_v.historys),
   path('time/',ab_v.time),
   path('doctorprofile/',ab_v.profile),
   path('booking/',ab_v.book),
]