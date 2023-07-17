from django.contrib import admin
from productos.models import Categorias, Productos, SubCategorias

admin.site.register(Productos)
admin.site.register(Categorias)
admin.site.register(SubCategorias)
