from django.shortcuts import render,redirect
from .forms import NotaForm
# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Notas(request):
    return render(request, 'tablero/notas.html')

def crearNota(request):
    if request.method == "POST":
        nota_form = NotaForm(request.POST)
        if nota_form.is_valid():
            nota_form.save()
            return redirect('notas')
    else:
        nota_form = NotaForm()
    return render(request, 'tablero/crear_nota.html',{'nota_form':nota_form})