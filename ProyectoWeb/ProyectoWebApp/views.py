from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User



def home(request):
    

    return render(request, 'ProyectoWebApp/home.html')

def destacados(request):

    return render(request, 'ProyectoWebApp/destacados.html' )

def crearBlog(request):

    return render(request, 'ProyectoWebApp/crear_blog.html' )

def contacto(request):

    return render(request, 'ProyectoWebApp/contacto.html' )

def perfil(request):

    return render(request, 'ProyectoWebApp/perfil.html' )

def busqueda(self):
   q = request.GET.get('q', '')
   eventos = user.objects.filter(user.username==q)
   return render(request, 'busqueda.html', {'eventos': eventos})