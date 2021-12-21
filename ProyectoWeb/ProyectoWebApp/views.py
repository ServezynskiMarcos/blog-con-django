from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from PostApp.models import Post



def home(request):
    

    return render(request, 'ProyectoWebApp/home.html')

def crearBlog(request):

    return render(request, 'ProyectoWebApp/crear_blog.html' )

def contacto(request):

    return render(request, 'ProyectoWebApp/contacto.html' )

def perfil(request):

    return render(request, 'ProyectoWebApp/perfil.html' )