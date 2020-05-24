from django.contrib import admin
from django.urls import path

from . import views, patient


urlpatterns = [
    path('product/', views.product),
    path('customer/', views.customer),
    path('aboutus/', views.aboutus),
    path('contact/', views.contact),
    path('patient_appointments/', patient.your_appointments),
    path('patient_invoice/', patient.invoice_and_payment),
    path('register/', views.registerPage,  name="register"),
    path('', views.home),
]