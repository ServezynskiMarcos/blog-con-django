from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('home/',views.home, name="Home"),
    path('categorias/',views.destacados, name="Categorias"),
    path('populares/',views.crearBlog, name="Populares"),
    path('contacto/',views.contacto, name="Contacto"),
    path('perfil/',views.perfil, name="Perfil"),
    
]
