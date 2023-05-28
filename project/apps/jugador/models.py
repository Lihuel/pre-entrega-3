from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    edad = models.IntegerField()
