from django.shortcuts import render, redirect
from .models import Materia
# Create your views here.

def Inicio_Vista(request):
    lasMaterias=Materia.objects.all()
    return render(request, "GestionarMateria.html",{"MisMaterias":lasMaterias})

def RegistarMateria(request):
    Codigo=request.POST["txtCodigo"]
    Nombre=request.POST["txtNombre"]
    Creditos=request.POST["numCreditos"]

    GuardarMateria=Materia.objects.create(
        Codigo=Codigo, Nombre=Nombre, Creditos=Creditos
    ) # Guarda el Registro

    return redirect("/")