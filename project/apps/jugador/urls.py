from . import views
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # path("",views.index, name ="index"),
    # path("crearjugador",views.crearjugador, name ="crearjugador"),
    # path("listajugador",views.listajugador, name ="listajugador"),
    path("", TemplateView.as_view(template_name="jugador/index.html"), name="index"),
    path("jugador/detail/<int:pk>", views.JugadorDetail.as_view(), name="jugador_detail"),
    path("jugador/list/", views.JugadorList.as_view(), name="jugador_list"),
    path("jugador/create/",(views.JugadorCreate.as_view()), name="jugador_create"),
    path("jugador/delete/<int:pk>", staff_member_required(views.JugadorDelete.as_view()), name="jugador_delete"),
    path("jugador/update/<int:pk>", staff_member_required(views.JugadorUpdate.as_view()), name="jugador_update"),
]