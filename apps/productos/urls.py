from django.urls import include, path

from . import views

app_name = "productos"

urlpatterns = [
    path("crear/", views.CrearProductos.as_view(), name="crear_productos"),
    path("productos/", views.ListProductos.as_view(), name="listar_productos"),
]
