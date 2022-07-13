from django.shortcuts import render
from django.views.generic import View
from .models import Manager, Group


                                                                   


def manager(request):
    managers= Manager.objects.all()
    integrantes = Group.objects.all()
    context = {
        'managers': managers,
        'integrantes': integrantes,
      }
 
    return render(request, 'comitiva/integrantes.html', context)

# Create your views here.
