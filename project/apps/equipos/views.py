from django.shortcuts import render, redirect
from . import forms
from .models import Equipo

def index(request):
    return render(request, "equipos/index.html")

def crearequipo(request):
   if request.method == "POST":
      form = forms.EquipoForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("equipos:index")
   form = forms.EquipoForm()
   context = {'form': form}
   return render(request, "equipos/crearequipo.html", context)

def listaequipo(request):
   lista_equipos = Equipo.objects.all()
   contexto = {'lista_equipos': lista_equipos}
   return render(request, "equipos/listaequipo.html", contexto)