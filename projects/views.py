from django.shortcuts import render
from django.http import HttpResponse

def trukea(request):
    return render(request,'index.html')

def IniciarSesion(request):
    return render(request,'iniciar_sesion.html')

def CrearCuenta(request):
    return render(request,'crear_cuenta.html')
# Create your views here.
