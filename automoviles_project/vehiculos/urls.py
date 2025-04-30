from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_automoviles, name='lista_automoviles'),
    path('crear/', views.crear_automovil, name='crear_automovil'),
    path('editar/<int:id>/', views.editar_automovil, name='editar_automovil'),
    path('eliminar/<int:id>/', views.eliminar_automovil, name='eliminar_automovil'),
]
