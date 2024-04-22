from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    # Campo para la imagen
    imagen = forms.ImageField(required=False)
    
    # Campo para el color
    COLORES = [
        ('#EA9E19', 'Amarillo'),  
        ('#54ea19', 'Verde'), 
        ('#19b6ea', 'Azul'),  
    ]
    color = forms.ChoiceField(choices=COLORES, initial='#ffffff')

    class Meta:
        model = Nota    
        fields = ('titulo', 'contenido', 'imagen', 'color')
