from django.shortcuts import render,redirect
from .models import Nota
from .forms import NotaForm
# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Notas(request):
    notas = Nota.objects.all()
    return render(request, 'tablero/notas.html',{'notas':notas})

def crearNota(request):
    if request.method == "POST":
        nota_form = NotaForm(request.POST)
        if nota_form.is_valid():
            nota_form.save()
            return redirect('notas')
    else:
        nota_form = NotaForm()
    return render(request, 'tablero/crear_nota.html',{'nota_form':nota_form})

