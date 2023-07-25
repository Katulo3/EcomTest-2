from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import AboutMeModel


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMeModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        # Debría agregar estos botones automáticamente
        # Dado que estoy usando vista basada en clases no lo muestra.
        self.helper.add_input(Submit("submit", "Guardar"))
