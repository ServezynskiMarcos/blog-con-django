from django.urls import path
from Users import views

urlpatterns = [
    path('registro/', views.Registro),
    path('prueba/', views.Prueba),
]
