from django.shortcuts import render
from django.views.generic import View
from .models import Formacion

                                                                         


def formacion(request):
    cursos= Formacion.objects.all()
    context = {
        'cursos': cursos,
      }
 
    return render(request, 'formacion/formacion.html', context)



