from django.db import models
from proyectoTablero import settings

# Create your models here.
class Nota (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True) # ESTA ES NUESTRA LLAVE PRIMARIA 
    titulo = models.CharField(max_length=50, blank=False, null=False) # Nuestro titulo no se puede quedar en blanco
    contenido = models.TextField(blank=False, null=False) # El contenido no puede ser vacio
    imagen = models.ImageField(upload_to='notas_imagenes/', null=True, blank=True) 
    COLORES = [
        ('#ff0000', 'Rojo'),  
        ('#00ff00', 'Verde'),  
        ('#0000ff', 'Azul'),  
    ]
    color = models.CharField(max_length=20, choices=COLORES, default='#ffffff')  

    def __str__(self):
        return self.titulo 
