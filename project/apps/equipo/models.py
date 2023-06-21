from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib import admin


admin.site.site_title = "Equipos"
admin.site.site_header = "La Liga de Fútbol"

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    cantidad_de_jugadores = models.IntegerField(default=0)
    cantidad_de_puntos = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de creación")
    class meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return f"{self.nombre_equipo}" 
    
    

   