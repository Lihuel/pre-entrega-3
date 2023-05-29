from django.shortcuts import render, redirect
from . import forms
from .models import Jugador

def index(request):
    return render(request, "jugador/index.html")

def crearjugador(request):
   if request.method == "POST":
      form = forms.JugadorForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("jugador:index")
   form = forms.JugadorForm()
   context = {'form': form}
   return render(request, "jugador/crearjugador.html", context)

def listajugador(request):
   return render(request, "jugador/listajugador.html")

def listajugador(request):
   lista_jugadores = Jugador.objects.all()
   contexto = {'lista_jugadores': lista_jugadores}
   return render(request, "jugador/listajugador.html", contexto)
