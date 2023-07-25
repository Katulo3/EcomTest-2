from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

app_name = "productos"

urlpatterns = [
    # CATEGORIAS
    path("crear/categorias/", views.crear_categorias, name="crear_categorias"),
    path("crear/editar_categorias/<int:pk>/", views.UpdateCategorias.as_view(), name="editar_categoria"),
    path("productos/eliminar_categoria/<int:pk>/", views.eliminar_categoria, name="eliminar_categoria"),
    # SUB CATEGORIAS
    path("crear/sub_categorias/", views.crear_sub_categorias, name="crear_subcategorias"),
    path("productos/eliminar_subcategoria/<int:pk>/", views.eliminar_subcategoria, name="eliminar_subcategoria"),
    path("crear/editar_subcategorias/<int:pk>/", views.UpdateSubCategorias.as_view(), name="editar_subcategoria"),
    # AMBAS
    path("sub_categorias/", views.sub_categorias, name="mostrar_categorias_subcategorias"),
    # Esto asegura que se carguen correctamente los archivos de static
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path("crear/", views.CrearProductos.as_view(), name="crear_productos"),
    path("productos/", views.ListProductos.as_view(), name="productos"),
    path("productos/eliminar_producto/<int:pk>/", views.eliminar_producto, name="eliminar_producto"),
    path("productos/editar_producto/<int:pk>/", views.UpdateProductos.as_view(), name="editar_producto"),
]
