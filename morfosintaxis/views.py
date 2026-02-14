from django.shortcuts import render, get_object_or_404
from .models import Leccion, Ejercicio

def index(request):
    lecciones = Leccion.objects.filter(activa=True)
    return render(request, 'morfosintaxis/index.html', {
        'total_lecciones': lecciones.count(),
    })

def lista_lecciones(request):
    lecciones = Leccion.objects.filter(activa=True)
    return render(request, 'morfosintaxis/lista_lecciones.html', {
        'lecciones': lecciones
    })

def leccion_detalle(request, numero):
    leccion = get_object_or_404(Leccion, numero=numero, activa=True)
    ejercicios = leccion.ejercicios.all()
    return render(request, 'morfosintaxis/leccion_detalle.html', {
        'leccion': leccion,
        'ejercicios': ejercicios
    })
