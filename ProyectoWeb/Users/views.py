from django.shortcuts import render
from django.http import HttpResponse

def Registro(request):
    return render(request, "form.html")

def Prueba(request):
    mensaje= "prueba %s" %request.GET["info"]
    return HttpResponse(mensaje)
