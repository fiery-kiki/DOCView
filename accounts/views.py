from django.shortcuts import render

from django.http import HttpResponse

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def get_receptionist():
    data = ['Total Appointments', 'Appointments Done', 'Upcoming Appointments']
    value = [1, 2, 3]
    arr = [{'title':data[i], 'value':value[i]} for i in range(len(data))]
    return arr

def get_hr():
    data = ['Total Doctors', 'Total Patients', 'On duty Doctors']
    value = [1, 2, 3]
    arr = [{'title':data[i], 'value':value[i]} for i in range(len(data))]
    return arr

def home(request):
    data = {
        'user_type': {'hr':0, 'receptionist':1, 'doctor':0, 'patient':0},
        }
    data['status_data'] = get_receptionist() if data['user_type']['receptionist'] else get_hr() if data['user_type']['hr'] else []
    return render(request, 'accounts/dashboard.html', data)




def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def product(request):
    return render(request, 'accounts/product.html')
