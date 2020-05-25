from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Patient, Doctor, Appointment, Prescription, Invoice

class CreatePatient(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'phone_no', 'gender', 'age', 'address', 'blood_group']

class CreateAppointment(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class CreatePrescription(ModelForm):
    class Meta:
        model = Prescription
        fields = ['prescription', 'disease', 'patient']

class CreateInvoice(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class CreateDoctor(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'phone_no', 'gender', 'age', 'address', 'status', 'department', 'attendance', 'salary']

object_choice = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient')
    )
class CreateUserForm(UserCreationForm):
    
    options = forms.ChoiceField(choices = list(object_choice))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

