from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User




def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, 'Te has resistrado con exito')
			return redirect('/home')

	
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)
