from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from PIL import Image, ImageFilter


class AboutMeModel(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    thumbnail = ImageSpecField(
        source="image", processors=[ResizeToFit(100, 100)], format="JPEG", options={"quality": 90}
    )
    titulo = models.CharField(max_length=50, default="titulo", null=False, blank=False)
    texto_presentacion = models.TextField(max_length=500, null=False, blank=False)

    class Meta:
        verbose_name = "Presentación de la empresa"
        verbose_name_plural = "Presentaciones de la empresa"

    def __str__(self):
        return self.titulo

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    # * Esto deberia permitir que se pueda editar el tamaño de la imagen por defecto sin front
    # * Como no funciona correctamente meto css y lo veo otro día en otro momento.
    # def resize_image(self):
    #     image = Image.open(self.image)
    #     image.thumbnail((300, 300))
    #     image.save(self.image.path)

    # def apply_antialias(self):
    #     # Example of applying antialiasing filter to the image using Pillow
    #     img = Image.open(self.image.path)
    #     antialiased_img = img.filter(ImageFilter.ANTIALIAS)
    #     antialiased_img.save(self.image.path)
    # * Ese es para el html
    # # <img src="{{ about_me.thumbnail.url }}" alt="Thumbnail">
