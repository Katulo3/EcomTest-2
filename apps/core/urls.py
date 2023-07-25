from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("about_me/", views.VerAboutMe.as_view(), name="about_me"),
    path("about_me_edit/", views.EditAboutMe.as_view(), name="editar_about_me"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
