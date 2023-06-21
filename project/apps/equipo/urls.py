from . import views
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [

    path("", TemplateView.as_view(template_name="equipo/index.html"), name="index"),
    path("equipo/detail/<int:pk>", views.EquipoDetail.as_view(), name="equipo_detail"),
    path("equipo/list/", views.EquipoList.as_view(), name="equipo_list"),
    path("equipo/create/",(views.EquipoCreate.as_view()), name="equipo_create"),
    path("equipo/delete/<int:pk>", staff_member_required(views.EquipoDelete.as_view()), name="equipo_delete"),
    path("equipo/update/<int:pk>", staff_member_required(views.EquipoUpdate.as_view()), name="equipo_update"),

 
]