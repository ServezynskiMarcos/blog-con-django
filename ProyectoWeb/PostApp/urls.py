from django.urls import path
from . import views
from .views import PostDetailView

urlpatterns = [
    #path('post/<int:id>', views.posteos, name="post"),
    #path('resultado_categoria/', views.post_categoria),
    #path('busqueda_categoria/', views.post_categoria),
    path('categorias/',views.destacados, name="Categorias"),
    #path('post/', views.posteos),
    #path('post/<int:pk>/', views.PostDetailView(),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
]