from django.urls import path
from . import views

urlpatterns = [
    path('trukea/', views.trukea,name="trukea"),
    path('inicioDeSesion/', views.IniciarSesion,name="IniciarSesion"),
    path('CrearCuenta/', views.CrearCuenta,name="CrearCuenta"),
    
]
