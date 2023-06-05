from django.db import models
from datetime import datetime


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titulo
    
    class meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'