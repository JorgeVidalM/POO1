from django.shortcuts import render, redirect, get_object_or_404
from .models import Automovil
from .forms import AutomovilForm

def lista_automoviles(request):
    autos = Automovil.objects.all()
    return render(request, 'vehiculos/lista.html', {'autos': autos})

def crear_automovil(request):
    if request.method == 'POST':
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_automoviles')
    else:
        form = AutomovilForm()
    return render(request, 'vehiculos/crear.html', {'form': form})

def editar_automovil(request, id):
    auto = get_object_or_404(Automovil, pk=id)
    if request.method == 'POST':
        form = AutomovilForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('lista_automoviles')
    else:
        form = AutomovilForm(instance=auto)
    return render(request, 'vehiculos/editar.html', {'form': form})

def eliminar_automovil(request, id):
    auto = get_object_or_404(Automovil, pk=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('lista_automoviles')
    return render(request, 'vehiculos/eliminar.html', {'auto': auto})
