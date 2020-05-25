from django.shortcuts import render, redirect 
from django.http import HttpResponse

from .models import Doctor, Patient, Appointment, Invoice, Prescription, Receptionist, HR

from .forms import CreateDoctor, CreatePatient, CreateUserForm, CreateAppointment

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required



def check_doctor(obj):
    return obj.__class__ == Doctor
def check_patient(obj):
    return obj.__class__ == Patient
def check_receptionist(obj):
    return obj.__class__ == Receptionist
def check_hr(obj):
    return obj.__class__ == HR
        



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            print('CHECK -' , request.POST)
            form = CreateUserForm(request.POST)
            if form.is_valid():
                print('VALIDATED')
                type_user = request.POST.get('options')
                u1 = form.save()
                # print(u1, type_user)
                u2 = None
                if type_user=='doctor':
                    u2 = Doctor.objects.create(user = u1)
                    u2.save()
                elif type_user=='patient':
                    u2 = Patient.objects.create(user = u1)
                    u2.save()
                print("CREATED peoples", u1, u2)
                messages.success(request, 'Account was created for ' + u1.username)
                return redirect('/')
        context = {'form':form}
        return render(request, 'accounts/register_patient.html', context)

@login_required(login_url='login')
def updatePatient(request, pk):
    p1 = Patient.objects.get(pk = pk)
    form = CreatePatient(instance=p1)
    if request.method == 'POST':
        form = CreatePatient(request.POST, instance=p1)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('user.username')
            # messages.success(request, 'Account was created for ' + user)
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/register_patient.html', context)

@login_required(login_url='login')
def deleteDoctor(request, pk):
    doctor = Doctor.objects.get(pk = pk)
    if request.method == "POST":
        doctor.delete()
        return redirect('/')
    context = {"item":doctor, 'obj_url':"delete_doctor"}
    return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
def updateDoctor(request, pk):
    p1 = Doctor.objects.get(pk = pk)
    form = CreateDoctor(instance=p1)
    if request.method == 'POST':
        form = CreateDoctor(request.POST, instance=p1)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('user.username')
            # messages.success(request, 'Account was created for ' + user)
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/register_doctor.html', context)

@login_required(login_url='login')
def deletePatient(request, pk):
    patient = Patient.objects.get(pk = pk)
    if request.method == "POST":
        patient.delete()
        return redirect('/')
    context = {"item":patient, 'obj_url':"delete_patient"}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def createAppointments(request):
    form = CreateAppointment()
    if request.method == 'POST':
        form = CreateAppointment(request.POST)
        if form.is_valid():
            a1 = form.save()
            print('appointment - ', a1)
            messages.success(request,"Successfully create appointment for {} with doctor {} at {}".format(a1.patient, a1.doctor, a1.date))
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/create_appointment.html', context)

    

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print('USER LOGGED IN', user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

def get_receptionist():
    data = ['Total Appointments', 'Appointments Done', 'Upcoming Appointments']
    ap1 = Appointment.objects.all()
    p1 = Patient.objects.all()
    value = [ap1.count(), ap1.filter(status = 'completed').count, ap1.filter(status = 'pending').count()]
    arr = [{'title':data[i], 'value':value[i]} for i in range(len(data))]
    return arr, {'appointment':ap1, 'patient':p1[:5]}

def get_hr():
    data = ['Total Doctors', 'Total Patients', 'On duty Doctors']
    d1 = Doctor.objects.all()
    p1 = Patient.objects.all()
    value = [d1.count(), p1.count(), d1.filter(status = 'active').count()]
    arr = [{'title':data[i], 'value':value[i]} for i in range(len(data))]
    return arr, {'doctor':d1, 'patient':p1[:5]}

@login_required(login_url='login')
def home(request):
    data = {
        'user_type': {'hr':0, 'receptionist':1, 'doctor':0, 'patient':0},
        }
    status, val = [], {}
    if data['user_type']['receptionist']:
        status, val = get_receptionist()
    elif data['user_type']['hr']:
        status, val = get_hr()
    data['status_data'] = status
    data.update(val)
    return render(request, 'accounts/dashboard.html', data)









def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def product(request):
    return render(request, 'accounts/product.html')
