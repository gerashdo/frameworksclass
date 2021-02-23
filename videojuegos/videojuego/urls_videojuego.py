from django.urls import path
from . import views

app_name = 'videojuego'

urlpatterns = [
    path('lista/', views.lista_videojuegos, name='lista_videojuegos'),
    path('nuevo/', views.nuevo_videojuego, name='nuevo_videojuego'),
    path('eliminar/<int:id>', views.eliminar_videojuego, name='eliminar_videojuego'),
    path('editar/<int:id>', views.editar_videojuego, name='editar_videojuego'),
]