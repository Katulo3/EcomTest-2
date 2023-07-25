from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="cuentas:login")
def index(request):
    fecha_hora = datetime.now()
    fecha_hora_f = fecha_hora.strftime(r"%d/%m/%Y , a las %H:%M:%Shs")
    datos = {"fecha_hora": fecha_hora_f}
    return render(request, "index.html", datos)
