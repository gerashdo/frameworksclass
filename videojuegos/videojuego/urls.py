from django.urls import path
from . import views

app_name = 'videojuego'

urlpatterns = [
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('eliminar-categoria/<int:id>', views.eliminar_categoria, name='eliminar_categoria'),
    path('lista-videojuegos/', views.lista_videojuegos, name='lista_videojuegos'),
    path('eliminar-videojuego/<int:id>', views.eliminar_videojuego, name='eliminar_videojuego')
]