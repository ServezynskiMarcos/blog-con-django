from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from registroApp import views



urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
	path('resultado_busqueda/',views.buscar),
	
]