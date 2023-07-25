from django.shortcuts import render
from productos.models import Productos


def tienda(request):
    productos = Productos.objects.all()
    contexto = {"productos": productos}
    return render(request, "Tienda/tienda.html", contexto)
