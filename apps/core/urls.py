from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("about_me/", views.about_me, name="about_me"),
]
