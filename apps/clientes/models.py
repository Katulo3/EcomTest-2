from django.contrib.auth.models import User
from django.db import models


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    nombre = models.CharField(max_length=50, verbose_name="Nombre", default="", null=False, blank=False)
    apellido = models.CharField(max_length=50, verbose_name="Apellido", default="", null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
