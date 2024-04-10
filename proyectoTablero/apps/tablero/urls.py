from django.urls import path
from .views import crearNota, Notas, editarNota

urlpatterns = [
    path('crear_nota/', crearNota, name='crear_nota'),
    path('notas/', Notas, name='notas' ),
    path('editar_nota/<int:id>', editarNota, name= 'editar_nota')
]