from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name ="index"),
    path("crearequipo",views.crearequipo, name ="crearequipo"),
    path("listaequipo",views.listaequipo, name ="listaequipo"),
]