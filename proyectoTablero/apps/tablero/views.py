from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NotaForm
from .models import Nota

# Esta función nos carga el arhivo raiz 
#  es la vista principal de la aplicación 
def Home(request):
    return render(request, 'index.html')

@login_required
def Notas(request):
    notas = Nota.objects.filter(usuario=request.user)
    return render(request, 'tablero/notas.html', {'notas': notas})

@login_required
def crearNota(request):
    if request.method == "POST":
        form = NotaForm(request.POST, request.FILES)
        print("Form data:", form.data)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario = request.user            
            nota.save()
            return redirect('notas')
        else:
            print("Form errors:", form.errors)
    else:
        form = NotaForm()        
    return render(request, 'tablero/crear_nota.html', {'form': form})


@login_required
def editarNota(request, id):
    nota = get_object_or_404(Nota, id=id, usuario=request.user)
    if request.method == 'POST':
        form = NotaForm(request.POST, request.FILES, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('notas')
        else:
            print("Formulario no válido:", form.errors)  # Impresión de depuración
    else:
        form = NotaForm(instance=nota)
    return render(request, 'tablero/crear_nota.html', {'form': form, 'nota': nota})



@login_required
def eliminarNota(request, id):
    nota = get_object_or_404(Nota, id=id, usuario=request.user)
    if request.method == 'POST':  # Asegúrate de que la eliminación se haga con un POST
        nota.delete()
        return redirect('notas')
    else:
        # Si no es un POST, puedes redirigir al usuario o mostrar un mensaje de error
        return redirect('notas')