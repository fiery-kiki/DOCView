from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def patientonly(view_func):
	def wrapper_func(request, *args, **kwargs):
		if not hasattr(request.user, 'patient'):
			return render(request, 'error_show.html', {
				'type':404,
				'message':'Invalid user type, not a patient'
			})
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def patientanddoctoronly(view_func):
	def wrapper_func(request, *args, **kwargs):
		if not (hasattr(request.user, 'patient') or hasattr(request.user, 'doctor')):
			return render(request, 'error_show.html', {
				'type':404,
				'message':'Invalid user type, not a patient'
			})
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def doctoronly(view_func):
	def wrapper_func(request, *args, **kwargs):
		if not (hasattr(request.user, 'doctor')):
			return render(request, 'error_show.html', {
				'type':404,
				'message':'Invalid user type, not a patient'
			})
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func
