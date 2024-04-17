from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Agregar mensaje de depuración
            print(f"Nuevo usuario creado: {user.username}")
            return redirect('notas')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('notas')  # Redirigir a la página de notas después del inicio de sesión
    else:
        form = CustomAuthenticationForm()
    return render(request, 'usuarios/iniciar_sesion.html', {'form': form})

def logout(request):
    django_logout(request)
    return redirect('index')  # Redirige a la página de inicio