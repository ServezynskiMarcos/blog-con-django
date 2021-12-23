from functools import cache
from django.shortcuts import render
from .models import Post, Comentario
from PostApp.forms import ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
def ExistePost(id):
    for i in cache.get('post'):
        if i.id == id:
            return i
    return None

def busqueda_post(request):
    return render(request, "busqueda_blog.html")

def destacados(request):

    return render(request, 'destacados.html' )

class PostDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = ComentarioForm()
        comment = Comentario.objects.filter(post=post)

        context = {
            'post': post,
            'form': form,
            'comment':comment
        }

        return render(request, 'resultados.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comment = Comentario.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comment':comment
        }

        return render(request, 'resultados.html', context)