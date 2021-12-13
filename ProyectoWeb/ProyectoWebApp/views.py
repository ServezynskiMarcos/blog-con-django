from django.shortcuts import render, HttpResponse

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
