from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import crearNota, Notas, editarNota, eliminarNota

#urlpatterns = [
#    path('crear_nota/', crearNota, name='crear_nota'),
#    path('notas/', Notas, name='notas' ),
#    path('editar_nota/<int:id>', editarNota, name= 'editar_nota'),
#    path('eliminar_nota/<int:id>', eliminarNota, name='eliminar_nota')
#]

urlpatterns = [
    path('crear_nota/', login_required(crearNota), name='crear_nota'),
    path('notas/', login_required(Notas), name='notas'),
    path('editar_nota/<int:id>', login_required(editarNota), name='editar_nota'),
    path('eliminar_nota/<int:id>', login_required(eliminarNota), name='eliminar_nota'),
]