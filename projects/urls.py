from django.urls import path
from . import views

urlpatterns = [
    path('trukea/', views.trukea,name="trukea"),
    path('iniciar_sesion/', views.IniciarSesion,name="iniciar_sesion"),
    path('CrearCuenta/', views.crearcuenta,name="CrearCuenta"),
    path('InicioCliente/', views.InicioCliente,name="InicioCliente"),
    path('AgregarDestinatario/', views.AgregarDestinatario,name="AgregarDestinatario"),
    path('ClienteTransaccion/', views.ClienteTransaccion,name="clienteTransaccion"),
    path('EnviarDinero/', views.EnviarDinero,name="EnviarDinero"),
    path('AgregarDinero/', views.AgregarDinero,name="AgregarDinero"),
    path('EliminarDestinatario/', views.EliminarDestinatario,name="EliminarDestinatario"),
    path('InicioAdministrador/', views.InicioAdministrador,name="InicioAdministrador"),
    path('ConsultarListaTransacciones/', views.ConsultarListaTransacciones,name="ConsultarListaTransacciones"),
    path('EditarMoneda/', views.EditarMoneda,name="EditarMoneda"),
    path('AdminEditarMoneda/', views.AdminEditarMoneda,name="AdminEditarMoneda"),
    path('AgregarMonedaPlataforma/', views.AgregarMonedaPlataforma,name="AgregarMonedaPlataforma"),
    path('ConsultarListaMonedas/', views.ConsultarListaMonedas,name="ConsultarListaMonedas"),
    path('ClienteListaTransacciones/', views.ClienteLIstaTransacciones,name="ClienteListaTransacciones"),
]

