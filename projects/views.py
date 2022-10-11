from faulthandler import cancel_dump_traceback_later
from django.shortcuts import render
from django.http import HttpResponse
from enum import auto
from inspect import Attribute
import re
import datetime
from xml.dom.minidom import Document
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import F

def trukea(request):
    return render(request,'index.html')

def IniciarSesion(request):
    return render(request,'iniciar_sesion.html')

def CrearCuenta(request):
    return render(request,'crear_cuenta.html')

def InicioCliente(request):
    return render(request,'inicio_cliente.html')

def AgregarDestinatario(request):
    return render(request,'agregar_destinatario.html')

def ClienteTransaccion(request):
    return render(request,'cliente_transaccion.html')

def EnviarDinero(request):
    return render(request,'enviar_dinero.html')

def AgregarDinero(request):
    return render(request,'agregar_dinero.html')

def EliminarDestinatario(request):
    return render(request,'eliminar_destinatario.html')
# Create your views here.
def projects(request):
    proyectos=models.Proyecto.objects.all()
    Usuario_reg=models.Usuario_registrado.objects.all()
    Users_orig=models.User.objects.all()
    Add_coin=models.Agregar_moneda.objects.all()
    return render(request, 'projects.html', {'proyectos':proyectos, 'Usuario_reg':Usuario_reg,
    'Users_orig':Users_orig,'Add_coin':Add_coin})

#def Usuarios_registrados(request):
#    Usuario_reg=models.Usuario_registrado.objects.all()
#    return render(request, 'projects.html', {'Usuario_reg':Usuario_reg})

@login_required(login_url='login')
def project(request):
    return render(request, 'single-project.html')

def crearcuenta(request):
    if request.method == 'POST':    
        username = request.POST['email']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        documento = request.POST['documento']
        moneda = request.POST['moneda']
        celular = request.POST['celular']
        ciudad = request.POST['ciudad']
        fechaexpedicion = request.POST['fechaexpedicion']
        pais = request.POST['pais']
        direccion = request.POST['direccion'] 
        tipodocumento = request.POST['tipodocumento']

        datos=request.POST
        print(datos)


        if User.objects.filter(username=username).exists():
            return HttpResponse("Error:El nombre de usuario ya existe")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("Error:El correo ya existe")
        else:  
        #crea el usuario
            user=User()
            user.is_active=1
            user.username = username
            user.set_password(password)
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            user2=models.Usuario_registrado()
            user2.usuario = user
            user2.documento=documento
            #user2.monedas=moneda
            user2.celular=celular
            user2.ciudad=ciudad
            user2.fechaexpedicion=fechaexpedicion
            user2.pais=pais
            user2.tipodocumento=tipodocumento
            user2.save()
        #return redirect('app:login')
    return render(request, 'crear_cuenta.html')


    success_url = reverse_lazy("login")
    template_name = "crear_cuenta.html"

def loginUser(request):

    if request.user.is_authenticated:
        return('projects')

    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        try:
            user= User.objects.get(username=username)
        except:
            #print('Username does not exist')
            #messages.error(request, 'Username does not exist')
            return HttpResponse("Error: el usuario no existe")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            #print('Username OR password is incorrect')
            #messages.error(request, 'Username OR password is incorrect')
            return HttpResponse("Error: Usuario o contraseña incorrecta")
            #success_message = "Username OR password"
    return render(request, 'iniciar_sesion.html')

def mainPage(request):
    return render(request, 'main.html')

def logoutUser(request):
    logout(request)
    #success_message = "IT was sucesfully logout"
    #messages.error(request, 'User was sucesfully logout')
    return HttpResponse("Logout Correcto")
    return redirect('iniciar_sesion.html')

def monedas(request):
    if request.user.is_superuser:
        return('projects')

    if request.method == 'POST':
        tasa =request.POST['tasa']
        moneda =request.POST['moneda']
        codigomoneda =request.POST['Codigo de la moneda']
    else:
        user3=models.monedas()
        user3.moneda=moneda
        user3.tasa=tasa
        user3.codigomoneda=codigomoneda
        user3.save()
        
    return render(request, 'iniciar_sesion.html')

