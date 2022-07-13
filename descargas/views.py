from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Reunion, Calendario, Permiso, Seguridad, Convenio



#class HomeView(View):
    #def get(self, request, *args, **kwargs):
        #context={
            
        #}
        #return render(request, 'index.html', context)                                                                          


def reunion(request):
    reuniones= Reunion.objects.all()
    context = {
        'reuniones': reuniones,
      }
 
    return render(request, 'descargas/reuniones.html', context)

def calendario(request):
    calendarios= Calendario.objects.all()
    context = {
        'calendarios': calendarios,
      }
 
    return render(request, 'descargas/calendarios.html', context)

def permisos(request):
    permisos= Permiso.objects.all()
    context = {
        'permisos': permisos,
      }
 
    return render(request, 'descargas/permisos.html', context)

def prevencion(request):
    prevenciones= Seguridad.objects.all()
    context = {
        'prevenciones': prevenciones,
      }
 
    return render(request, 'descargas/prevencion.html', context)

def convenio(request):
    convenios= Convenio.objects.all()
    context = {
        'convenios': convenios,
      }
 
    return render(request, 'descargas/convenio.html', context)
  
  

