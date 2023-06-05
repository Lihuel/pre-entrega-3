from django.contrib import admin
from . import models

admin.site.site_title = "Equipos"
admin.site.site_header = "La Liga de Fútbol"

@admin.register(models.Equipo)
class   Equipo(admin.ModelAdmin):
    """
    - list_display: tupla que especifica los campos que se mostrarán en la lista de objetos
    - search_fields: tupla que especifica los campos por los que se puede buscar en la lista de objetos
    - list_filter: tupla que especifica los campos por los que se puede filtrar en la lista de objetos
    - ordering: tupla que especifica el orden en que se mostrarán los objetos
    """

    list_display = ("nombre_equipo", "cantidad_de_jugadores")
    search_fields = ("nombre_equipo",)
    list_filter = ("nombre_equipo",)
    ordering = ("nombre_equipo",)