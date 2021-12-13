from django import forms

from ProyectoWeb.Users.models import Usuarios

class FormularioRegistro(forms.ModelForm):
    
    class Meta:
        model = Usuarios
        fields = ("__all__")