#  * Apps
from email import message

from cuentas.forms import CreateUserForm, UserCreationForm

# * django contrib
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# * django views
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from apps.cuentas.forms import EditUserForm

# * django imports


# Mostrar clientísimos
# class ListClientes(ListView):
#     model = Cliente
#     template_name = "clientes/clientes.html"
#     fields = "__all__"

#     def listar_clientes(self, **kwargs):
#         # Hereda  y extiende el contexto de la clase
#         contexto = super().get_context_data(**kwargs)

#         clientes = Cliente.objects.all()
#         contexto["clientes"] = clientes
#         return contexto

#     # Ordena en un query los clientes por orden alfabético del nombre
#     def get_queryset(self):
#         orden = super().get_queryset().order_by("nombre")
#         return orden


# class CrearCliente(CreateView):
#     model = Cliente
#     template_name = "clientes/crud_clientes.html"
#     success_url = reverse_lazy("clientes")
#     fields = "__all__"


# class EditarCliente(UpdateView):
#     model = Cliente
#     template_name = "clientes/crud_clientes.html"
#     success_url = reverse_lazy("clientes")
#     fields = "__all__"


# # class EliminarCliente(DeleteView):
# #     model = Cliente
# #     template_name = "clientes/crud_cliente.html"
# #     success_url = reverse_lazy("list_clientes")


class VerUsuarios(ListView):
    model = User
    template_name = "cuentas/usuarios.html"

    def listar_usuarios(self, **kwargs):
        # Hereda  y extiende el contexto de la clase
        contexto = super().get_context_data(**kwargs)

        usuarios = User.objects.all()
        contexto["usuarios"] = usuarios
        return contexto


def registrar_usuarios(request):
    # Evita que el usuario navege en registrar y login si ya ingresó
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # Ver mensaje
                user = form.cleaned_data.get("username")
                messages.success(request, f"Usuario creado exitosamente:{user}")
                return redirect("cuentas:login")

        contexto = {"form": form}
        return render(request, "cuentas/registrar.html", contexto)


def login_usuario(request):
    # Evita que el usuario navege en registrar y login si ya ingresó
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        contexto = {}
        return render(request, "cuentas/login.html", contexto)


@login_required(login_url="cuentas:login")
def logout_usuario(request):
    logout(request)
    return redirect("index")


@login_required(login_url="cuentas:login")
def perfil(request):
    contexto = {}
    user = User.objects.all()
    contexto["user"] = user
    return render(request, "perfil.html", contexto)


class EditarPerfil(UpdateView):
    template_name = "cuentas/crear.html"
    model = User
    form_class = EditUserForm

    success_url = reverse_lazy("cuentas:login")
