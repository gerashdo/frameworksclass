from django.urls import path
from . import views

app_name = 'videojuego'

urlpatterns = [
    path('lista/', views.lista_videojuegos, name='lista_videojuegos'),
    path('eliminar/<int:id>', views.eliminar_videojuego, name='eliminar_videojuego')
]