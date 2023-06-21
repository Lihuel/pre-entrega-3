from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import forms, models

def index(request):
    return render(request, "jugador/index.html")

class JugadorCreate(CreateView):
    model = models.Jugador
    form_class = forms.JugadorForm
    success_url = reverse_lazy("jugador:index")


class JugadorList(ListView):
    model = models.Jugador

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Jugador.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Jugador.objects.all()
        return object_list


class JugadorDetail(DetailView):
    model = models.Jugador


class JugadorDelete(DeleteView):
    model = models.Jugador
    success_url = reverse_lazy("jugador:jugador_list")


class JugadorUpdate(UpdateView):
    model = models.Jugador
    success_url = reverse_lazy("jugador:jugador_list")
    form_class = forms.JugadorForm
