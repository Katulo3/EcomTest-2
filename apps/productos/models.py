from tabnanny import verbose

from django.core.validators import MinValueValidator
from django.db import models


class Categorias(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre", default="", null=True, blank=False)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        app_label = "productos"

    def __str__(self):
        return f"{self.nombre}"


class SubCategorias(models.Model):
    categoria = models.ForeignKey(
        Categorias, max_length=50, verbose_name="Nombre", on_delete=models.SET_NULL, null=True, blank=False
    )
    nombre = models.CharField(max_length=50, verbose_name="Nombre", default="", null=True, blank=False)

    class Meta:
        verbose_name = "Subcategoria"
        verbose_name_plural = "Subcategorias"
        app_label = "productos"

    def __str__(self):
        return f"{self.nombre}"


class Productos(models.Model):
    nombre_categoria = models.ForeignKey(Categorias, max_length=50, on_delete=models.SET_NULL, null=True, blank=False)
    nombre_subcategoria = models.ForeignKey(
        SubCategorias, max_length=50, on_delete=models.SET_NULL, null=True, blank=False
    )

    nombre = models.CharField(max_length=50, verbose_name="Nombre", default="", null=False, blank=False)
    precio = models.DecimalField(
        verbose_name="Precio", max_digits=10, blank=False, decimal_places=2, validators=[MinValueValidator(0)]
    )
    stock = models.IntegerField(default=0, verbose_name="Stock", null=False, blank=False)
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    digital = models.BooleanField(default=False, null=False, blank=False)
    descripcion = models.TextField(max_length=250, null=False, blank=False)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        app_label = "productos"

    def __str__(self):
        return f"{self.nombre}"
