from django.contrib import admin
from . import models

admin.site.site_title = "Jugadores"
admin.site.site_header = "La Liga de Fútbol"


@admin.register(models.Jugador)
class  Jugador(admin.ModelAdmin):
      list_display = ("nombre", "edad", "posicion", "equipo")
      search_fields = ("nombre",)
      list_filter = ("nombre",)
      list_display_links = ("nombre",)
      ordering = ("nombre", "edad",)

