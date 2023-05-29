from django.db import models
from equipos.models import *

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=100, blank=True, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

