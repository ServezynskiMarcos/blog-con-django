from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:id>', views.posteos, name="post"),

]