from django.urls import path
from tabla_multiplicar import views

urlpatterns = [
    path('tabla-multiplicar/', views.tabla_multiplicar),
]