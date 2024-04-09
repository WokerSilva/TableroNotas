from django.db import models

# Create your models here.
class Nota (models.Model):
    id = models.AutoField(primary_key=True) # ESTA ES NUESTRA LLAVE PRIMARIA 
    titulo = models.CharField(max_length=50, blank=False, null=False) # Nuestro titulo no se puede quedar en blanco
    contenido = models.TextField(blank=False, null=False) # El contenido no puede ser vacio