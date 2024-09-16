from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('driver_form/', views.driver_form, name='driver_form'),
]
