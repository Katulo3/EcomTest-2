from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from productos.models import Productos

# carpetas de apps


class CrearProductos(CreateView):
    model = Productos
    template_name = "productos/crear.html"
    success_url = reverse_lazy("productos")
    fields = "__all__"


class ListProductos(ListView):
    model = Productos
    template_name = "productos/productos.html"
    fields = "__all__"

    def listar_productos(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        productos = Productos.objects.all()
        contexto["productos"] = productos
        return contexto
