from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from registroApp.forms import UserRegisterForm
from django.contrib.auth.models import User




def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, 'Te has resistrado con exito')
			return redirect('/login')

	
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

def buscar(request):
    if request.GET["nombre"]:
        name= request.GET["nombre"]

        if len(name) > 20:
            mensaje="Ha sobrepasado el numero de caracteres maximos permitidos"
            print(mensaje)
        
        else:
            
            user = User.objects.filter(username__icontains=name)
            
            return render(request, "social/resultado_busqueda.html", {"nombre":user, "query":name})
    else:
        
        mensaje = "No has ingresado nada"
        return HttpResponse(mensaje)

            

	
        

	
        
