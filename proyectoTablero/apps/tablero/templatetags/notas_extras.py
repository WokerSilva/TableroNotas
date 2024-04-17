# notas/templatetags/notas_extras.py
from django import template

register = template.Library()

@register.filter(name='add_color')
def add_color(value):
    """Agrega el color de fondo a la tarjeta."""
    return f'style="background-color: {value};"'
