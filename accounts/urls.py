from django.contrib import admin
from django.urls import path

from . import views, patient, doctor


urlpatterns = [
    path('product/', views.product),
    path('customer/', views.customer),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('profile/', patient.profilePage, name='profile'),
    path('accounting/', views.accounting, name='accounting'),
    path('patient_appointments/', patient.your_appointments, name="your_appointments"),
    path('patient_invoice/', patient.invoice_and_payment, name='invoice_and_payment'),
    path('pacient_med_history', patient.medical_history, name='medical_history'),
    path('doctor_appointments/', doctor.your_appointments, name="doc_appointments"),
    # basic auth
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('register_patient/', views.registerPatient,  name="register_patient"),
    # path('register_doctor/', views.registerDoctor,  name="register_doctor"),
    path('create_appointment/', views.createAppointments, name='create_appointment'),
    path('create_prescription/<str:dpk>/', views.createPrescriptions, name='create_prescription'),
    path('create_invoice/', views.createInvoices, name='create_invoice'),
    path('update_patient/<str:pk>/', views.updatePatient,  name="update_patient"),
    path('delete_patient/<str:pk>/', views.deletePatient,  name="delete_patient"),
    path('update_doctor/<str:pk>/', views.updateDoctor,  name="update_doctor"),
    path('delete_doctor/<str:pk>/', views.deleteDoctor,  name="delete_doctor"),
    path('detail_invoice/<str:pk>', patient.invoice_detailed, name="detail_invoice"),
    path('', views.home, name='home'),
]