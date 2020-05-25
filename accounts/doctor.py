from django.shortcuts import render, redirect
from .models import Appointment, Invoice, Patient, Prescription
from django.contrib.auth.decorators import login_required
from .forms import CreateDoctor, CreatePatient
from .decorators import *
from .patient import value_convertor

@doctoronly
@login_required(login_url='login')
def your_appointments(request):
    data = {}
    data['title'] = ['Date', 'Time', 'Patient Info']
    data['value'] = [ ]
    u1 = request.user
    p1 = u1.doctor
    if hasattr(p1, 'appointment_set'):
        for apt in p1.appointment_set.all():
            data['value'].append([ apt.date, apt.time, apt.patient])
    type = ['text', 'text', 'text']
    data['value'] = [ value_convertor(row, type) for row in data['value']]
    return render(request, 'accounts/your_appointments.html', {'data':data})
