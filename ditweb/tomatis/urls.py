from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices/',views.devices, name='devices'),
    path('config/',views.config, name='config'),
    path('verify_result/',views.verify_result, name='verify_result'),
    path('log/',views.log, name='log'),
    path('otomatis/',views.otomatis, name='otomatis'),
    path('sdn/',views.sdn, name='sdn'),
    path('about/',views.about, name='tentang'),
    path('nmap/',views.NMap, name='nmap'),
    path('dummy/',views.dummy, name='dummy'),
]