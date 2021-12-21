from django.urls import path
from . import views

urlpatterns = [
    #path('post/<int:id>', views.posteos, name="post"),
    path('resultado_categoria/', views.post_categoria),
    path('busqueda_categoria/', views.busqueda_post),
    path('categorias/',views.destacados, name="Categorias"),
]