from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "clientes"

urlpatterns = [
    path("clientes/", views.ListClientes.as_view(), name="clientes"),
    path("crud_clientes/", views.CrearCliente.as_view(), name="crear_cliente"),
    path("editar_cliente/<pk>/", views.EditarCliente.as_view(), name="editar_cliente"),
    path("usuarios/", views.VerUsuarios.as_view(), name="usuarios"),
]
