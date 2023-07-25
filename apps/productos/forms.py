# crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from productos.models import Categorias, SubCategorias

# apps
from .models import Productos


class ProductosForm(forms.ModelForm):
    image = forms.ImageField(
        label="Imagen",
        required=True,
    )
    digital = forms.ChoiceField(
        choices=((1, "Sí"), (0, "No")),
        widget=forms.RadioSelect(),
        initial=0,
        required=True,
    )
    stock = forms.IntegerField(
        label="Stock",
        required=True,
    )

    class Meta:
        model = Productos
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


# Estos dos forms podría haberlos hecho sin usar forms.py pero quería reutilizar el html
class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        # Esto va así para que si cambio el nombre en models no se rompa esto y tenga que cambiarlo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


class SubCategoriasForm(forms.ModelForm):
    class Meta:
        model = SubCategorias
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
