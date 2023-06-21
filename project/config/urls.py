from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("equipo/", include(("equipo.urls", "equipo"))),
    path("jugador/", include(("jugador.urls", "jugador"))),
    path("noticias/", include(("noticias.urls", "noticias"))),
]
