from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "Tienda"

urlpatterns = [
    path("tienda/", views.tienda, name="tienda"),
]
