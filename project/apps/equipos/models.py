from django.db import models

from django.db import models

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    cantidad_de_jugadores = models.IntegerField()

    def __str__(self):
        return self.nombre_equipo