from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
<<<<<<< HEAD
from registroApp import views
=======
>>>>>>> 732b6feb14bda8c0de7b1637c5c386b277fa1276



urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
<<<<<<< HEAD
	path('resultado_busqueda/',views.buscar),
=======
>>>>>>> 732b6feb14bda8c0de7b1637c5c386b277fa1276
	
]