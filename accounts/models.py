from django.db import models
from django.contrib.auth.models import User

gender_choice = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)
blood_choice = (
    ('a_positive', 'A+ Type'),
    ('a_negative', 'A- Type'),
    ('b_positive', 'B+ Type'),
    ('b_negative', 'B- Type'),
    ('ab_positive', 'AB+ Type'),
    ('ab_negative', 'AB- Type'),
    ('o_positive', 'O+ Type'),
    ('o_negative', 'O- Type'),
)
# Create your models here.

class Receptionist(models.Model):
    user = models.OneToOneField(User, verbose_name="receptionist", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name ="Receptionist"
        verbose_name_plural = "Receptionists"

    def __str__(self):
        return self.user.username

class HR(models.Model):
    user = models.OneToOneField(User, verbose_name="hr", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name ="HR"
        verbose_name_plural = "HRs"

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    
    user = models.OneToOneField(User, verbose_name="patient", on_delete=models.CASCADE)
    name = models.CharField( max_length=50, null = True, blank = True)
    phone_no = models.CharField( max_length=10, null = True, blank = True)
    gender = models.CharField( max_length=10, null = True, blank = True, choices = gender_choice)
    age = models.IntegerField(null = True, blank = True)
    address = models.CharField( max_length=100, null = True, blank = True)
    blood_group = models.CharField( max_length=30, null = True, blank = True, choices = blood_choice)
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        return super(Patient, self).save(*args, **kwargs)

class Doctor(models.Model):
    status_choice = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )
    user = models.OneToOneField(User, verbose_name="doctor", on_delete=models.CASCADE)
    name = models.CharField( max_length=50, null = True, blank = True)
    phone_no = models.CharField( max_length=10, null = True, blank = True)
    gender = models.CharField( max_length=10, null = True, blank = True, choices = gender_choice)
    age = models.IntegerField(null = True, blank = True)
    address = models.CharField( max_length=100, null = True, blank = True)
    status = models.CharField( max_length=100, null = True, blank = True, choices = status_choice)
    department = models.CharField( max_length=20, null = True, blank = True)
    attendance = models.IntegerField(null = True, blank = True)
    salary = models.IntegerField(null = True, blank = True)
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        return super(Doctor, self).save(*args, **kwargs)


class Appointment(models.Model):
    status_choices = (
        ('pending', 'Pending'),
        ('completed', 'Completed')
        )
    patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, verbose_name="doctor", on_delete=models.CASCADE)
    date = models.DateField( auto_now=False, auto_now_add=False)
    time = models.TimeField( auto_now=False, auto_now_add=False)
    status = models.CharField( max_length=50, choices = status_choices, null=False)
    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return '{} -> {}'.format(self.patient, self.doctor)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, verbose_name="doctor", on_delete=models.CASCADE)
    prescription = models.CharField( max_length=50)
    disease = models.CharField( max_length=50)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Prescription"
        verbose_name_plural = "Prescriptions"

    def __str__(self):
        return '{} -> {}'.format(self.patient, self.doctor)

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    unit_cost = models.IntegerField()
    date = models.DateField( auto_now_add=True)
    hours = models.IntegerField()
    paid = models.IntegerField( null=True, blank=True)
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def get_outstanding(self):
        return self.hours*self.unit_cost - self.paid

    def __str__(self):
        return self.name

