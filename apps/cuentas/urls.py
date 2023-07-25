from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "cuentas"

urlpatterns = [
    # Clientes
    # path("clientes/", views.ListClientes.as_view(), name="clientes"),
    # path("crud_clientes/", views.CrearCliente.as_view(), name="crear_cliente"),
    # path("editar_cliente/<pk>/", views.EditarCliente.as_view(), name="editar_cliente"),
    # # Users
    path("usuarios/", views.VerUsuarios.as_view(), name="usuarios"),
    path("registrar/", views.registrar_usuarios, name="registrar_usuarios"),
    path("login/", views.login_usuario, name="login"),
    path("logout/", views.logout_usuario, name="logout"),
    path("perfil/", views.perfil, name="perfil"),
    path("crear/editar_perfil/<pk>", views.EditarPerfil.as_view(), name="editar_perfil"),
]
