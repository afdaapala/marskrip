from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('devices/',views.devices),
    path('config/',views.config),
    path('verify_result/',views.verify_result),
    path('log/',views.log),
    path('otomatis/',views.otomatis),
    path('sdn/',views.sdn),
    path('about/',views.about),
    path('nmap/',views.NMap),
]