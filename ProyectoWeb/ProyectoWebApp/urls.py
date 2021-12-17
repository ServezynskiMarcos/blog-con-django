from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('home/',views.home, name="Home"),
    path('categorias/',views.destacados, name="Categorias"),
    path('populares/',views.crearBlog, name="Populares"),
    path('contacto/',views.contacto, name="Contacto"),
<<<<<<< HEAD
=======
    path('busqueda/',views.busqueda, name="Busqueda"),
    
>>>>>>> 732b6feb14bda8c0de7b1637c5c386b277fa1276
]
