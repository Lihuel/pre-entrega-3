from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name ="index"),
    path("crearjugador",views.crearjugador, name ="crearjugador"),
    path("listajugador",views.listajugador, name ="listajugador"),
]