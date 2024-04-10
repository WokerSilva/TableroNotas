from django.contrib import admin
# añadimos el modelo nota
from .models import Nota

admin.site.register(Nota)