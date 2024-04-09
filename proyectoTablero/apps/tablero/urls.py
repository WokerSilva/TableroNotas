from django.urls import path
from .views import crearNota, Notas

urlpatterns = [
    path('crear_nota/', crearNota, name='crear_nota'),
    path('notas/', Notas, name='notas' )
]