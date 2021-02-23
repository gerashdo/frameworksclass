from django.shortcuts import render, redirect
from .models import Categoria, Videojuego
from .form_categoria import CategoriaForm

# CATEGORIAS
def lista_categoria(request):
    categorias= Categoria.objects.all()
    return render(request,'lista_categorias.html',{'categorias':categorias})

def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categoria:lista_categoria')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista_categoria')
    context = {
        'form' : form
    }     
    return render(request,'editar_categoria.html',context)

def nuevo_categoria(request):
    form = CategoriaForm

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista_categoria')

    context = {
        'form' : form
    }
    return render(request,'nuevo_categoria.html',context )


# VIDEOJUEGOS
def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request,'lista_videojuegos.html',{'videojuegos':videojuegos})

def eliminar_videojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    videojuego.delete()
    return redirect('videojuego:lista_videojuegos')