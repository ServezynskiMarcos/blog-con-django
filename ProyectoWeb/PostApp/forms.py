from django import forms

from .models import Comentario

class ComentarioForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'placa',
            'rows': '1',
            'placeholder': 'Comentar'
            }),
        required=True
        )
    class Meta:
        model= Comentario
        fields=['comment']