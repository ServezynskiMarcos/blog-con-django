from functools import cache
from django.shortcuts import render, redirect

from PostApp.forms import ComentarioForm
from .models import *


def posteos(request, id):
    try:
        posts = ExistePost(id)
    except Exception:
        posts = Post.objects.filter(id=id)
    coments = Comentario.objects.filter(post=id)

    form = ComentarioForm(request.POST or None)
    if form.is_valid():
            if request.user.is_authenticated:
                aux = form.save(commit=False)
                aux.post = posts
                aux.user = request.user
                aux.save()
                form = ComentarioForm()
            else:
                return redirect('usuario:login')

    context = {
        'posts': posts,
        'coments': coments,
    }
    return render(request, 'post.html', context)


def ExistePost(id):
    for i in cache.get('posts'):
        if i.id == id:
            return i
    return None
