from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import NotaForm
from .models import Nota

# Esta función nos carga el arhivo raiz 
#  es la vista principal de la aplicación 
def Home(request):
    return render(request, 'index.html')

# Esta función carga el archivo de notas 
#  y tambien hace la lista de las notas en la BD
def Notas(request):
    notas = Nota.objects.all()
    return render(request, 'tablero/notas.html',{'notas':notas})

# Esta función carga la pagina para crear las notas
def crearNota(request):
    if request.method == "POST":
        nota_form = NotaForm(request.POST)
        if nota_form.is_valid():
            nota_form.save()
            return redirect('notas')
    else:
        nota_form = NotaForm()
    return render(request, 'tablero/crear_nota.html',{'nota_form':nota_form})

def editarNota(request, id):
    nota_form = None
    error = None
    # Manejamos el error de no encontrar el id 
    try:
        nota = Nota.objects.get(id = id)        
        if request.method == 'GET':
            nota_form = NotaForm(instance = nota)
        else:
            nota_form = NotaForm(request.POST, instance = nota)
            if nota_form.is_valid():
                nota_form.save()
            return redirect('notas')    
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'tablero/crear_nota.html',{'nota_form':nota_form,'error':error})