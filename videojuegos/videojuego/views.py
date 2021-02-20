from django.shortcuts import render, redirect
from .models import Categoria, Videojuego

# Create your views here.

def lista_categorias(request):
    categorias= Categoria.objects.all()
    return render(request,'lista_categorias.html',{'categorias':categorias})

def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('videojuego:lista_categorias')

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request,'lista_videojuegos.html',{'videojuegos':videojuegos})

def eliminar_videojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    videojuego.delete()
    return redirect('videojuego:lista_videojuegos')