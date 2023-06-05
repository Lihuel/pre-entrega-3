from django.db import models
from equipos.models import *
from django.contrib import admin


admin.site.site_title = "Jugadores"
admin.site.site_header = "La Liga de Fútbol"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=100, blank=True, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True)

    class meta:
       verbose_name = "Jugador"
       verbose_name_plural = "Jugadores"

    def __str__(self):
        return self.nombre
    
    



