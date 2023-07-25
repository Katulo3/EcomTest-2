from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import AboutMeForm
from .models import AboutMeModel


class VerAboutMe(ListView):
    model = AboutMeModel
    template_name = "core/about_me.html"

    def about_me(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        prensentacion = AboutMeModel.objects.all()
        contexto["prensentacion"] = prensentacion
        return contexto


class EditAboutMe(CreateView):
    model = AboutMeModel
    template_name = "about_me_edit.html"
    form_class = AboutMeForm
    success_url = reverse_lazy("core:about_me")
