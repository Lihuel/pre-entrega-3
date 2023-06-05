from django.contrib import admin
from . import models

admin.site.site_title = "Noticias"
admin.site.site_header = "La Liga de Fútbol"

admin.site.register(models.Noticia)