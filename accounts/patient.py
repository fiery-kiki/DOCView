from django.shortcuts import render, redirect
from .models import Appointment, Invoice, Patient, Prescription
from django.contrib.auth.decorators import login_required
from .forms import CreateDoctor, CreatePatient
from .decorators import *
def value_convertor(row, type):
    value = []
    for j in range(len(row)):
        value.append({'value':row[j], 'type':type[j]})
    return value

@patientonly
@login_required(login_url='login')
def your_appointments(request):
    data = {}
    data['title'] = ['Date', 'Time', 'Consulting Doctor', 'Status']
    data['value'] = [ ]
    u1 = request.user
    p1 = u1.patient
    if hasattr(p1, 'appointment_set'):
        for apt in p1.appointment_set.all():
            data['value'].append([ apt.date, apt.time, apt.doctor, apt.status])
    type = ['text', 'text', 'text', 'text']
    data['value'] = [ value_convertor(row, type) for row in data['value']]
    return render(request, 'accounts/your_appointments.html', {'data':data})

@patientonly
@login_required(login_url='login')
def invoice_and_payment(request):
    data = {}
    data['title'] = ['Invoice', 'Paid', 'Date', 'Outstanding']
    data['value'] = [ ]
    u1 = request.user
    p1 = u1.patient
    if hasattr(p1, 'invoice_set'):
        for inv in p1.invoice_set.all():
            data['value'].append([
                inv,
                inv.paid,
                inv.date,
                inv.get_outstanding()
                ])
    data['obj_url'] = "detail_invoice"
    type = ['link', 'text', 'text', 'text']
    data['value'] = [ value_convertor(row, type) for row in data['value']]
    return render(request, 'accounts/your_appointments.html', {'data':data})


@login_required(login_url='login')
def invoice_detailed(request, pk):
    i1 = Invoice.objects.get(pk = pk)
    return render(request, 'accounts/detail_invoice.html', {'invoice':i1})


#for patient and doctors
@patientanddoctoronly
@login_required(login_url='login')
def profilePage(request):
    u1 = request.user
    formclass = CreateDoctor
    if hasattr(u1, 'patient'):
        p1 = u1.patient
        formclass = CreatePatient
    elif hasattr(u1, 'doctor'):
        p1 = u1.doctor
    else:
        return render(request, 'error_show.html', {
            'type':404,
            'message':'Invalid user type, neither a doctor or patient'
        })
    form = formclass(instance=p1)
    if request.method == 'POST':
        form = formclass(request.POST, instance=p1)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('user.username')
            # messages.success(request, 'Account was created for ' + user)
            return redirect('/')
    context = {'form':form, 'title':"Welcome {}".format(p1)}
    return render(request, 'accounts/profile.html', context)

#medical History
@patientanddoctoronly
@login_required(login_url='login')
def medical_history(request):
    u1 = request.user
    if hasattr(u1, 'patient'):
        p1 = u1.patient
    else:
        p1 = u1.doctor
    prc = []
    if hasattr(p1, 'prescription_set'):
        print(p1, 'has prc')
        prc = p1.prescription_set.all()
    return render(request, 'accounts/medical_history.html', {
        'prescriptions':prc
    } )


