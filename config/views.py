from datetime import datetime

from django.shortcuts import render


def index(request):
    fecha_hora = datetime.now()
    fecha_hora_f = fecha_hora.strftime(r"%d/%m/%Y , a las %H:%M:%Shs")
    datos = {"fecha_hora": fecha_hora_f}
    return render(request, "index.html", datos)
