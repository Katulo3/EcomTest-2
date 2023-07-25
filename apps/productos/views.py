from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from productos.models import Categorias, Productos, SubCategorias

from apps import productos

from .forms import CategoriasForm, ProductosForm, SubCategoriasForm


class CrearProductos(CreateView):
    model = Productos
    template_name = "productos/crear.html"
    form_class = ProductosForm
    success_url = reverse_lazy("productos:productos")


class UpdateProductos(UpdateView):
    model = Productos
    template_name = "productos/crear.html"
    form_class = ProductosForm
    success_url = reverse_lazy("productos:productos")

    def get_pk(self, pk):
        producto = Productos.objects.get(id=pk)
        return producto


class ListProductos(ListView):
    model = Productos
    template_name = "productos/productos.html"
    fields = "__all__"

    def get_queryset(self):
        query = self.request.GET.get("buscar")
        if query:
            productos = Productos.objects.filter(nombre__icontains=query)
            if not productos:
                messages.warning(self.request, "No se encontraron resultados")
            return productos
        else:
            productos = Productos.objects.all()
        return productos


def eliminar_producto(request, pk):
    producto = Productos.objects.get(id=pk)
    producto.delete()
    messages.success(request, "Se ha eliminado el producto exitosamente.")
    return redirect("productos:productos")


# Ordenar por nombre
# * Ver después
# def ordenar_productos(self, request):
#     sort_by = self.request.POST.get("sort_criteria")

#     if sort_by == "nombre":
#         orden = self.get_queryset().order_by("nombre")
#         print("Se ha elegido ordenar por nombre")
#     elif sort_by == "precio":
#         orden = self.get_queryset().order_by("nombre")
#         print("Se ha elegido ordenar por precio")
#     elif sort_by == "categoria":
#         orden = self.get_queryset().order_by("nombre")
#         print("Se ha elegido ordenar por categoría")
#     else:
#         orden = self.get_queryset().order_by("nombre")
#         print("Se ha elegido ordenar por subcategoría")

#     return (request, {"data": orden}, "productos/productos.html")


# * Muestra todas las subcategorías y categorías en un solo template
def sub_categorias(request):
    contexto = {}
    categorias = Categorias.objects.all()
    sub_categorias = SubCategorias.objects.all()
    contexto["categorias"] = categorias
    contexto["sub_categorias"] = sub_categorias

    return render(request, "productos/sub_categorias.html", contexto)


def crear_categorias(request):
    form = CategoriasForm()

    if request.method == "POST":
        form = CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            # Ver mensaje
            categoria = form.cleaned_data.get("categoria_name")
            messages.success(request, f"Categoria creada exitosamente: {categoria}")
            return redirect("index")

    contexto = {"form": form}
    return render(request, "productos/crear.html", contexto)


class UpdateCategorias(UpdateView):
    model = Categorias
    template_name = "productos/crear.html"
    form_class = CategoriasForm
    success_url = reverse_lazy("index")

    def get_pk(self, pk):
        categoria = Categorias.objects.get(id=pk)
        return categoria


def eliminar_categoria(request, pk):
    categoria = Categorias.objects.get(id=pk)
    categoria.delete()
    messages.success(request, "Se ha eliminado la categoria exitosamente.")
    return redirect("index")


# SUB CATEGORIAS
class UpdateSubCategorias(UpdateView):
    model = SubCategorias
    template_name = "productos/crear.html"
    form_class = SubCategoriasForm
    success_url = reverse_lazy("index")

    def get_pk(self, pk):
        subcategoria = SubCategorias.objects.get(id=pk)
        return subcategoria


def crear_sub_categorias(request):
    form = SubCategoriasForm()

    if request.method == "POST":
        form = SubCategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            # Ver mensaje
            subcategoria = form.cleaned_data.get("sub_categoria")
            messages.success(request, f"Subcategoria creada exitosamente:{subcategoria}")
            return redirect("index")

    contexto = {"form": form}
    return render(request, "productos/crear.html", contexto)


def eliminar_subcategoria(request, pk):
    sub_categoria = SubCategorias.objects.get(id=pk)
    sub_categoria.delete()
    messages.success(request, "Se ha eliminado la subcategoria exitosamente.")
    return redirect("index")
