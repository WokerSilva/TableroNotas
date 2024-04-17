from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    # Campo para la imagen que no es obligatoria
    imagen = forms.ImageField(required=False)
    
    # Campo para el color
    COLORES = [
        ('#ff0000', 'Rojo'),  
        ('#00ff00', 'Verde'),  
        ('#0000ff', 'Azul'),  
    ]
    color = forms.ChoiceField(choices=COLORES, initial='#ffffff')

    class Meta:
        model = Nota    
        fields = ('titulo', 'contenido', 'imagen', 'color')
