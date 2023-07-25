from django.core.validators import MinValueValidator
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Categorias(models.Model):
    categoria_name = models.CharField(max_length=50, verbose_name="Nombre", default="", null=True, blank=False)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        app_label = "productos"

    def __str__(self):
        return f"{self.categoria_name}"


class SubCategorias(models.Model):
    categoria = models.ForeignKey(
        Categorias, max_length=50, verbose_name="Nombre", on_delete=models.CASCADE, null=True, blank=False
    )
    sub_categoria = models.CharField(max_length=50, verbose_name="Nombre", default="", null=False, blank=False)

    class Meta:
        verbose_name = "Subcategoria"
        verbose_name_plural = "Subcategorias"
        app_label = "productos"

    def __str__(self):
        return f"{self.sub_categoria}"


class Productos(models.Model):
    nombre_categoria = models.ForeignKey(Categorias, max_length=50, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_subcategoria = models.ForeignKey(
        SubCategorias, max_length=50, on_delete=models.SET_NULL, null=True, blank=True
    )

    nombre = models.CharField(max_length=50, verbose_name="Nombre", default="", null=False, blank=False)
    precio = models.DecimalField(
        verbose_name="Precio", max_digits=10, blank=False, decimal_places=2, validators=[MinValueValidator(0)]
    )
    stock = models.PositiveSmallIntegerField(default=0, verbose_name="Stock", null=True, blank=True)
    image = models.ImageField(upload_to="productos", null=False, blank=False, default=None)
    image_thumbnail = ImageSpecField(
        source="image", processors=[ResizeToFit(300, 300)], format="PNG", options={"quality": 90}
    )
    digital = models.BooleanField(default=False, null=False, blank=False)
    descripcion = models.TextField(max_length=250, null=True, blank=True)

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        app_label = "productos"

    def __str__(self):
        return f"{self.nombre}"
