from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import forms, models

def index(request):
    return render(request, "equipo/index.html")

class EquipoCreate(CreateView):
    model = models.Equipo
    form_class = forms.EquipoForm
    success_url = reverse_lazy("equipo:index")


class EquipoList(ListView):
    model = models.Equipo

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Equipo.objects.filter(nombre_equipo__icontains=query)
        else:
            object_list = models.Equipo.objects.all()
        return object_list


class EquipoDetail(DetailView):
    model = models.Equipo


class EquipoDelete(DeleteView):
    model = models.Equipo
    success_url = reverse_lazy("equipo:equipo_list")


class EquipoUpdate(UpdateView):
    model = models.Equipo
    success_url = reverse_lazy("equipo:equipo_list")
    form_class = forms.EquipoForm
