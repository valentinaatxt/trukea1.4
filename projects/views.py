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
from django.contrib.auth.hashers import make_password

def trukea(request):
    return render(request,'index.html')


def CrearCuenta(request):
    return render(request,'crear_cuenta.html')

def InicioCliente(request):
    template='inicio_cliente.html'
    print(request.user.id)
    user_data=models.Usuario_registrado.objects.get(usuario=request.user.id)
    return render(request,'inicio_cliente.html',{'user_data':user_data})



def AgregarDestinatario(request):
    if request.method == 'POST':    
        username = request.POST['email']
        email = request.POST['email']
        documento = request.POST['documento']
        tipodocumento = request.POST['tipodocumento']
        user=models.Destinatarios()
        user.email=email
        user.documento=documento
        user.tipodocumento=tipodocumento
        user.save()
        if User.objects.filter(username=username).exists():
           user2= User.objects.filter(username=email).values_list('first_name','last_name')
           firstname=user2[0][0]
           lastname=user2[0][1]
           return HttpResponse("nombre:"+firstname+"apellido:"+lastname)
        else:
            return HttpResponse("Error:El usuario no existe")
        
    return render(request,'agregar_destinatario.html')

def ClienteTransaccion(request):
    return render(request,'cliente_transaccion.html')

def EnviarDinero(request):
    return render(request,'enviar_dinero.html')

def AgregarDinero(request):
    return render(request,'agregar_dinero.html')

def EliminarDestinatario(request):
    return render(request,'eliminar_destinatario.html')

def InicioAdministrador(request):
    return render(request,'inicio_administrador.html')

def HabilitarDeshabilitarMoneda(request):
    return render(request,'habilitar_deshabilitar_moneda.html')

def ConsultarListaTransacciones(request):
    return render(request,'consultar_lista_transacciones.html')

def EditarMoneda(request):
    return render(request,'editar_moneda.html')

def AdminEditarMoneda(request):
    return render(request,'admin_editar_moneda.html')

def AgregarMonedaPlataforma(request):

    moneda=None
    tasa=None
    codigomoneda=None


    if request.method == 'POST':
        print(request.POST)
        tasa =request.POST['tasa']
        moneda =request.POST['moneda']
        codigomoneda =request.POST['codigomoneda']
        user3=models.monedas()
        user3.moneda=moneda
        user3.tasa=tasa
        user3.codigomoneda=codigomoneda
        user3.save()
            #success_message = "Username OR password"
    return render(request, 'agregar_moneda_plataforma.html')


def ConsultarListaMonedas(request):
    return render(request,'consultar_lista_monedas.html')

def ClienteLIstaTransacciones(request):
    return render(request,'cliente_lista_transacciones.html')

def ConsultarListaMonedas(request):
    return render(request,'cliente_lista_monedas.html')
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
        password = make_password(request.POST['password'])
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
            user.username = email
            user.password = password
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

def IniciarSesion(request):

    #if request.user.is_authenticated:
        #return('projects')

    if request.method == 'POST':
        username =request.POST['email']
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
            if  username=='valen@gmail.com':
                return redirect('InicioAdministrador')
            else:
                return redirect('InicioCliente')
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

