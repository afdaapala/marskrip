from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('otomatis/',views.otomatis),
    path('sdn/',views.sdn),
]