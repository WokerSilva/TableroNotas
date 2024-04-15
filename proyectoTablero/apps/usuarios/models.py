from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser (AbstractUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    fecha_nacimiento = models.DateField()

    
    def __str__(self):
        return self.nombre  # Devuelve el nombre de usuario al imprimir el objeto

