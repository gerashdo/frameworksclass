
from django.urls import path
from hola_mundo import views


urlpatterns = [
    path('hola-mundo/', views.hola_mundo),
    path('ingenieria/', views.ingenieria, name='ing'),
]