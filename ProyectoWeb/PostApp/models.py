from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .utils.enum.categorias import *


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image

    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    titulo = models.CharField(max_length=250)
    fecha = models.DateField(default= timezone.now)
    texto = models.TextField(max_length = 10000)
    categoria = models.CharField(max_length=40, choices=Categorias, default='Pobreza')
    image = models.ImageField(upload_to='imag_blog', null=True)


    def __str__(self):
        return f'{self.user.username}: {self.titulo}'


# Create your models here.
class Comentario(models.Model):
    
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=40, choices=Categorias, null=True)
    

