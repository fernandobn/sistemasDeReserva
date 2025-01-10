from django.shortcuts import render, get_object_or_404, redirect
from .models import Campista, Reserva
from .forms import CampistaForm, ReservaForm

# ---------------------
# Vistas para Campistas
# ---------------------

def lista_campistas(request):
    campistas = Campista.objects.all()
    return render(request, 'campistas/lista.html', {'campistas': campistas})


def detalle_campista(request, pk):
    campista = get_object_or_404(Campista, pk=pk)
    return render(request, 'campistas/detalle.html', {'campista': campista})


def nuevo_campista(request):
    if request.method == 'POST':
        form = CampistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_campistas')
    else:
        form = CampistaForm()
    return render(request, 'campistas/editar.html', {'form': form})


def editar_campista(request, pk):
    campista = get_object_or_404(Campista, pk=pk)
    if request.method == 'POST':
        form = CampistaForm(request.POST, instance=campista)
        if form.is_valid():
            form.save()
            return redirect('lista_campistas')
    else:
        form = CampistaForm(instance=campista)
    return render(request, 'campistas/editar.html', {'form': form})


def eliminar_campista(request, pk):
    campista = get_object_or_404(Campista, pk=pk)
    campista.delete()
    return redirect('lista_campistas')

# ---------------------
# Vistas para Reservas
# ---------------------

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista.html', {'reservas': reservas})


def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reservas/detalle.html', {'reserva': reserva})


def nueva_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/editar.html', {'form': form})


def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/editar.html', {'form': form})


def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('lista_reservas')
